from django.db import models

# Create your models here.
class Tweetdata(models.Model):
    id_str = models.CharField(max_length=40)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=16, decimal_places=8)
    latitude = models.DecimalField(max_digits=16, decimal_places=8)