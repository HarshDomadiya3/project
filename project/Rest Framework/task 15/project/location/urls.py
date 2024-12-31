from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_coordinates, name='get_coordinates'),
]
import requests

def get_coordinates(address):
    api_key = "AIzaSyCjw6mJVkK-lsvt6-OD8hVUuB6mobLoPj0"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    
    response = requests.get(url)
    data = response.json()

    if data.get('status') == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"Error: {data.get('status')} - {data.get('error_message', 'No additional information')}")
        return None
