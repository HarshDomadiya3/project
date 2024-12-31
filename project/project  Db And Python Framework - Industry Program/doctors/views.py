from django.shortcuts import render
from .models import Doctor

def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/index.html', {'doctors': doctors})

def index(request):
    return render(request, 'doctors/index.html')