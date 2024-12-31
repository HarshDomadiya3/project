from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings
from .forms import AddressForm

def get_coordinates(request):
    form = AddressForm()
    coordinates = None
    error_message = None

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            api_key = settings.GOOGLE_MAPS_API_KEY
            url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
            response = requests.get(url)
            data = response.json()

            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                coordinates = {
                    'latitude': location['lat'],
                    'longitude': location['lng']
                }
            else:
                error_message = "Invalid address or API error."

    return render(request, 'location/index.html', {
        'form': form,
        'coordinates': coordinates,
        'error_message': error_message
    })
