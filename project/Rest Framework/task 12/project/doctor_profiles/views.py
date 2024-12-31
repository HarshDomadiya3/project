from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

# View to list all doctors
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# View to retrieve, update, or delete a specific doctor
class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
