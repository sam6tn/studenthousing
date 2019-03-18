import datetime

from django.db import migrations
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

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
    def __str__(self):
        return self.name

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])