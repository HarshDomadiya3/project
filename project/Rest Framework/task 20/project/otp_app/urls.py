from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify-otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
]
