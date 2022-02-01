from django.shortcuts import (
    render, get_object_or_404, get_list_or_404, redirect
)

from .models import Country, City
from .forms import CountryForm, CityForm


def index(request):
    return render(request, 'index.html')


def country_list(request):
    countries = get_list_or_404(Country)
    return render(request, 'country_list.html', {'countries': countries})


def city_list(request, country):
    country = get_object_or_404(Country, name=country)
    cities = country.cities.all()
    return render(request, 'city_list.html', {'cities': cities})


def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city_detail.html', {'city': city})


def add_country(request):
    header = 'Add Country'
    action = 'Add'
    form = CountryForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_country = form.save(commit=False)
        new_country.save()
        return redirect('cities:country_list')
    return render(
        request,
        'new_country.html',
        {'form': form, 'header': header, 'action': action}
    )
