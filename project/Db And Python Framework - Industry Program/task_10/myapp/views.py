from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})
