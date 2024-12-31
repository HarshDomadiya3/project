from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('api/doctor/', views.doctor_list, name='doctor-list'),
 ]
