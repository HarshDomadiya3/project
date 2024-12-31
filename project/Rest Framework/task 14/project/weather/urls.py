from django.urls import path
from .views import fetch_weather

urlpatterns = [
    path('', fetch_weather, name='fetch_weather'),
]
