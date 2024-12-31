from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
