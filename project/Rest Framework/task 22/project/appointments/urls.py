

from django.urls import path
from . import views

urlpatterns = [
    path('doctor-locations/', views.doctor_locations, name='doctor_locations'),
]
