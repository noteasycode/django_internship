from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Country, City


def index(request):
    return render(request, 'index.html')


def country_list(request):
    countries = get_list_or_404(Country)
    return render(request, 'country_list.html', {'countries': countries})


def city_list(request, country):
    country = get_object_or_404(Country, name=country)
    cities = City.objects.filter(country=country)
    return render(request, 'city_list.html', {'cities': cities})
