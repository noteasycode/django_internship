from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import (
    render, get_object_or_404, get_list_or_404, redirect
)

from .models import Country, City
from .forms import CountryForm, CityForm


def index(request):
    return render(request, 'index.html')


def country_list(request):
    countries = get_list_or_404(Country)
    paginator = Paginator(countries, settings.PAGES_OBG_AMT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'country_list.html', {'page': page})


def city_list(request, country):
    country = get_object_or_404(Country, name=country)
    mcdonalds_value = request.GET.get('with_mcdonalds')
    if mcdonalds_value:
        cities = country.cities.filter(with_mcdonalds=mcdonalds_value)
    else:
        cities = country.cities.all()
    paginator = Paginator(cities, settings.PAGES_OBG_AMT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'country': country}
    return render(request, 'city_list.html', context)


def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city_detail.html', {'city': city})


@login_required()
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
        'new.html',
        {'form': form, 'header': header, 'action': action}
    )


@login_required()
def edit_country(request, country_id):
    header = 'Edit'
    action = 'Save'
    country = get_object_or_404(Country, pk=country_id)
    form = CountryForm(
        request.POST or None,
        files=request.FILES or None,
        instance=country
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cities:country_list')

    context = {
        'form': form, 'country': country, 'header': header, 'action': action,
        'country_id': country_id,
    }
    return render(request, 'new.html', context)


@staff_member_required()
def delete_country(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    country.delete()
    return redirect('cities:country_list')


@login_required()
def add_city(request, country):
    header = 'Add City'
    action = 'Add'
    country = get_object_or_404(Country, name=country)
    form = CityForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_city = form.save(commit=False)
        new_city.country = country
        new_city.save()
        return redirect('cities:city_list', country=country.name)
    return render(
        request,
        'new.html',
        {'form': form, 'header': header, 'action': action}
    )


@login_required()
def edit_city(request, city_id):
    header = 'Edit'
    action = 'Save'
    city = get_object_or_404(City, pk=city_id)
    form = CityForm(
        request.POST or None,
        files=request.FILES or None,
        instance=city
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cities:city_list', country=city.country)

    context = {
        'form': form, 'city': city, 'header': header, 'action': action,
        'city_id': city_id,
    }
    return render(request, 'new.html', context)


@staff_member_required()
def delete_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    city.delete()
    return redirect('cities:city_list', country=city.country)
