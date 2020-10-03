from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfCountries, particularCountry

urlpatterns = [
    path(r'countries/', listOfCountries.as_view()),
    path(r'countries/<int:pk>/', particularCountry.as_view()),
    # path(r'countries/', login_required(listOfCountries.as_view())),
    # path(r'countries/<int:pk>/', login_required(particularCountry.as_view())),

]
