from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_form, name='home'), 
    path('success/', views.success_page, name='success'),  
]
