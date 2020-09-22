from django.contrib import admin
from django.urls import path, include
from .api.views import listOfCountries, Country

urlpatterns = [
    path(r'countries/', listOfCountries.as_view()),
    path(r'countries/<int:pk>/', Country.as_view()),

]
