from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('tests/', views.redirect),
    path('tests/<int:pk>/', views.exponentiation),
]

