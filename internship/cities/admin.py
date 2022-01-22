from django.contrib import admin
from . models import Country, City


class CountryAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author')
    search_fields = ('name',)
    empty_value_display = '-empty-'


class CityAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author')
    search_fields = ('name',)
    list_filter = ('country', 'with_mcdonalds')
    empty_value_display = '-empty-'


admin.site.register(Country, CountryAdmin, City, CityAdmin)
