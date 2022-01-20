from django.shortcuts import render

from .database import CITY_DATABASE


def index(request):
    return render(request, 'index.html')


def country_list(request):
    countries = [country for country in CITY_DATABASE.keys()]
    return render(request, 'country_list.html', {'countries': countries})
