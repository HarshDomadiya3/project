from django.urls import path
from .views import AddDoctorView

urlpatterns = [
    path('add/', AddDoctorView.as_view(), name='add-doctor'),
]
