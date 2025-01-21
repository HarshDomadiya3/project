from django.db import models

# Create your models here.

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    specialty = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
