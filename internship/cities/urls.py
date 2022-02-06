from django.urls import path

from . import views


app_name = 'cities'

urlpatterns = [
    path('', views.index, name='index'),
    path('country_list/', views.country_list, name='country_list'),
    path('city_list/<country>/', views.city_list, name='city_list'),
    path('city_detail/<int:pk>/', views.city_detail, name='city_detail'),
    path('add_country/', views.add_country, name='add_country'),
    path('edit_country/<int:country_id>', views.edit_country, name='edit_country'),
    path('delete_country/<int:country_id>', views.delete_country, name='delete_country'),
    path('add_city/<country>', views.add_city, name='add_city'),
    path('edit_city/<int:city_id>', views.edit_city, name='edit_city'),
    path('delete_city/<int:city_id>', views.delete_city, name='delete_city'),
]
