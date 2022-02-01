from django.urls import path

from . import views


app_name = 'cities'

urlpatterns = [
    path('', views.index, name='index'),
    path('country_list/', views.country_list, name='country_list'),
    path('city_list/<country>/', views.city_list, name='city_list'),
    path('city_detail/<int:pk>/', views.city_detail, name='city_detail'),
    path('add_country/', views.add_country, name='add_country'),
]
