from django.shortcuts import render


import requests


def home(request):
    return render(request, 'countryinfo/home.html')

def get_country_info(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        url = f"https://restcountries.com/v3.1/name/{country}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            country_data = data[0]
            details = {
                'name': country_data.get('name', {}).get('common', 'N/A'),
                'population': country_data.get('population', 'N/A'),
                'language': ', '.join(country_data.get('languages', {}).values()),
                'currency': ', '.join([f"{curr} ({info.get('name')})"
                                       for curr, info in country_data.get('currencies', {}).items()])
            }
            return render(request, 'countryinfo/result.html', {'details': details})
        else:
            return render(request, 'countryinfo/result.html', {'error': 'Invalid country or API error.'})
    return render(request, 'countryinfo/home.html')
