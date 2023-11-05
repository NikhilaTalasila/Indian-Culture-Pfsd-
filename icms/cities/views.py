from django.shortcuts import render, redirect
from .models import City

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})

def city_redirect(request, city_id):
    city = City.objects.get(pk=city_id)
    return redirect(city.external_url)
