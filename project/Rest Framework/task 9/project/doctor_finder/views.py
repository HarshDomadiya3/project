# doctor_finder/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'  
    max_page_size = 100  

class DoctorListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()  
        paginator = DoctorPagination()  
        result_page = paginator.paginate_queryset(doctors, request) 
        serializer = DoctorSerializer(result_page, many=True)  
        return paginator.get_paginated_response(serializer.data)  
