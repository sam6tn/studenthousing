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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # area = models.CharField(max_length=100, blank=True)
    phone = models.CharField(default='', max_length=20)
    image = models.ImageField(default='avatar.jpg', upload_to='')

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

    # google_address = map_fields.AddressField(max_length=200, default="")
    # geolocation = map_fields.GeoLocationField(max_length=100, default="1207 Wertland Street")

    def __str__(self):
        return self.name

class Review(models.Model):
    profile_pic = models.CharField(default='',max_length=400)
    reviewer_name = models.CharField(default = '', max_length=100)
    reviewer_username = models.CharField(default = '', max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])