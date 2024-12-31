from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()  # All doctors ko fetch kar rahe hain
    return render(request, 'app/doctor_list.html', {'doctors': doctors})
