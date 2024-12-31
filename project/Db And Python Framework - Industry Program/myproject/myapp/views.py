

# Create your views here.
from django.shortcuts import render

# Example index view
def index(request):
    return render(request, 'index.html')
