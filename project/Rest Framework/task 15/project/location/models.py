from django.db import models

# Create your models here.
from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
