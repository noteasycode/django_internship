from django.urls import path
from . import views


urlpatterns = [
    path('', views.redirect),
    path('<int:pk>/', views.exponentiation),
]

