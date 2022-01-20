from django.shortcuts import render

from database import CITY_DATABASE


def index(request):
    return render(request, 'index.html')


def country_list(request):
    return render(request, 'country_list.html')
