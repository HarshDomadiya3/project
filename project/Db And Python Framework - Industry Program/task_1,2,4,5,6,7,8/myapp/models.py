from django.db import models

# Create your models here.
class students(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
  