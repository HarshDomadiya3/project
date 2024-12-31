# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_profiles, name='doctor_profiles'),
    path('add/', views.add_doctor_profile, name='add_doctor_profile'),
    path('edit/<int:pk>/', views.edit_doctor_profile, name='edit_doctor_profile'),
    path('delete/<int:pk>/', views.delete_doctor_profile, name='delete_doctor_profile'),
]
