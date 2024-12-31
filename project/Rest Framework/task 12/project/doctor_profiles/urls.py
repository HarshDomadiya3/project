from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),  # GET to list, POST to create
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-retrieve-update-destroy'),  # GET, PUT, DELETE for a specific doctor
]
