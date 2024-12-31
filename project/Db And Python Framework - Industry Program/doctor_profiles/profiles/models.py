from django.db import models

# Create your models here.
# profiles/models.py


class DoctorProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"
