from django.urls import path
from .views import admin_dashboard
from .views import customer_registration
from .views import customer_login
from .views import customer_registration_success
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('customer-registration/', customer_registration, name='customer_registration'),
    path('customer-login/', customer_login, name='customer_login'),
    path('customer-registration-success/', customer_registration_success, name='customer_registration_success'),
]



urlpatterns += [
    # Forgot password URL
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='insurance/forgot_password.html'), name='password_reset'),
    
    # Email sent confirmation page
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='insurance/password_reset_done.html'), name='password_reset_done'),

    # Password reset confirmation (link sent to the user's email)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='insurance/password_reset_confirm.html'), name='password_reset_confirm'),
    
    # Password successfully reset page
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='insurance/password_reset_complete.html'), name='password_reset_complete'),
]
