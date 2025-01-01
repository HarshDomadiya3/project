from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .utils import send_confirmation_email

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_confirmation_email(user.email, user.username)
            return render(request, 'users/registration_success.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
