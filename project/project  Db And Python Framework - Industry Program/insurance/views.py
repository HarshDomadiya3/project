from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .utils import send_confirmation_email
from .models import User, PolicyHolder

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

       
        user = User(username=username, email=email, password=password)
        user.save()

        
        send_confirmation_email(email)

        return redirect('login') 
    return render(request, 'insurance/register.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return redirect('dashboard') 
            else:
                return render(request, 'insurance/login.html', {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'insurance/login.html', {'error': 'User does not exist'})
    return render(request, 'insurance/login.html')

def dashboard(request):
   
    users = User.objects.all()
    policy_holders = PolicyHolder.objects.all()
    return render(request, 'insurance/dashboard.html', {'users': users, 'policy_holders': policy_holders})

