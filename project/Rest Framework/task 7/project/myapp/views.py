from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()  
        paginator = PageNumberPagination() 
        result_page = paginator.paginate_queryset(doctors, request)  
        serializer = DoctorSerializer(result_page, many=True) 
        return paginator.get_paginated_response(serializer.data)  
