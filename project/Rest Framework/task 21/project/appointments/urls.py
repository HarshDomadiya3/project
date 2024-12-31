from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('payment/<int:appointment_id>/', views.make_payment, name='make_payment'),
    path('paypal/<int:appointment_id>/', views.paypal_payment, name='paypal_payment'),
]
