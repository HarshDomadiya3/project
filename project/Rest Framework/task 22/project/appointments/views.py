
from django.shortcuts import render
from .models import Doctor
import googlemaps
from django.conf import settings

def doctor_locations(request):
   
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

   
    doctors = Doctor.objects.all()

   
    for doctor in doctors:
        if doctor.city:
            
            geocode_result = gmaps.geocode(doctor.city)
            if geocode_result:
                doctor.latitude = geocode_result[0]['geometry']['location']['lat']
                doctor.longitude = geocode_result[0]['geometry']['location']['lng']
                doctor.save()

  
    context = {
        'doctors': doctors
    }

    return render(request, 'appointments/doctor_locations.html', context)
