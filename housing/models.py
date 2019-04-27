import datetime


from django.db import migrations
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_google_maps import fields as map_fields
from django_google_maps.fields import AddressField, GeoLocationField

# for latitude and longitude
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # area = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    image = models.ImageField(default='avatar.jpg', upload_to='')
    need_roommate = models.BooleanField(default=True)
    YEAR_CHOICES = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Graduate Student'),
    )
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default="1")

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
           Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()


class Post(models.Model):
    name = models.CharField(default='',max_length=40)
    info = models.CharField(default='',max_length=200)
    address = models.CharField(default='No Address Found',max_length=100)
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    image_url = models.URLField(null=True)
    baths = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)

    # Override save method to update latitude and longitude information
    def save(self, *args, **kwargs):
        if not self.id:
            self.name = 'unknown'
        ctx = ssl.create_default_context(cafile=certifi.where())
        geopy.geocoders.options.default_ssl_context = ctx
        nom = Nominatim(scheme = 'http', user_agent='housing',timeout=10)
        location = nom.geocode(self.address)
        if (location):
            self.lat = location.latitude
            self.lng = location.longitude
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Review(models.Model):
    profile_pic = models.CharField(default='',max_length=400)
    reviewer_name = models.CharField(default = '', max_length=100)
    reviewer_username = models.CharField(default = '', max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(null=True)