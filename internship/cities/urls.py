from django.urls import path
from . import views


app_name = 'cities'

urlpatterns = [
    path('', views.index, name='index'),
    path('country_list', views.country_list, name='country_list')
]
