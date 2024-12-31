from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DoctorUpdateView(generics.UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DoctorDeleteView(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
