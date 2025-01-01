from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import PolicyHolder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_dashboard(request):
    users = User.objects.all()
    policy_holders = PolicyHolder.objects.all()
    return render(request, 'insurance/admin_dashboard.html', {
        'users': users,
        'policy_holders': policy_holders
    })


def customer_registration_success(request):
    return render(request, 'insurance/registration_success.html')

def customer_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        policy_type = request.POST['policy_type']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        PolicyHolder.objects.create(user=user, policy_type=policy_type)
        return redirect('customer_registration_success')
    
    return render(request, 'insurance/customer_registration.html')



def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to the dashboard after login
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'insurance/customer_login.html')
