from django import forms
from django.forms import Textarea

from .models import Country, City


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ('name', 'country_code', 'population', 'flag')
        labels = {
            'name': ('Name'),
            'country_code': ('Country code ISO 3166'),
            'population': ('Population'),
            'flag': ('Upload flag of country')
        }


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'description', 'population', 'emblem', 'with_mcdonalds')
        labels = {
            'name': ('Name'),
            'description': ('Description'),
            'population': ('Population'),
            'emblem': ('Upload emblem of the city'),
            'with_mcdonalds': ('Is McDonald\'s in this city?')
        }
        widgets = {
                    'description': Textarea(attrs={"class": "form-control"}),
                }