from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Doctor API Home Page")


@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()  
        serializer = DoctorSerializer(doctors, many=True) 
        return Response(serializer.data)  
    
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)  
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Welcome to the Doctor API</h1><p>Go to <a href='/api/doctors/'>Doctors API</a></p>")
