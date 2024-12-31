from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_country_info/', views.get_country_info, name='get_country_info'),
]
