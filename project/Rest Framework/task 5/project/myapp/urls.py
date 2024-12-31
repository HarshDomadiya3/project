from django.urls import path
from . import views

urlpatterns = [
    path('doctor/create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/update/<int:pk>/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    path('doctor/delete/<int:pk>/', views.DoctorDeleteView.as_view(), name='doctor-delete'),
]
