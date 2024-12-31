from django.db import models



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient_name} with Dr. {self.doctor.name}"
