from django.shortcuts import render
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

# View to list all doctors (GET request)
class DoctorListView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# View to retrieve, update, or delete a single doctor (GET, PUT, DELETE)
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
