from django.shortcuts import render

import requests


def get_weather(request):
    if request.method == "POST":
        city = request.POST.get("city").strip()
        print(f"City entered: {city}")  # Debugging

        api_key = "39098d6124755c7a34f337690ccd6d50"  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        print(f"API Response Status Code: {response.status_code}")  # Debugging
        print(f"API Response: {response.json()}")  # Debugging
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            return render(request, 'weather/weather.html', {'weather_data': weather_data})
        else:
            error_message = "City not found or invalid API response."
            return render(request, 'weather/weather.html', {'error': error_message})
    return render(request, 'weather/weather.html')


def fetch_weather(request):
    if request.method == "POST":
        city = request.POST.get("city")
        api_key = "39098d6124755c7a34f337690ccd6d50"  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            return render(request, 'weather/weather.html', {'weather_data': weather_data})

        else:
            error_message = "City not found or invalid API response."
            return render(request, 'weather/weather.html', {'error': error_message})
    return render(request, 'weather/weather.html')
