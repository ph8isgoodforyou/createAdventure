from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfCountries, Country

urlpatterns = [
    path(r'countries/', login_required(listOfCountries.as_view())),
    path(r'countries/<int:pk>/', login_required(Country.as_view())),

]
