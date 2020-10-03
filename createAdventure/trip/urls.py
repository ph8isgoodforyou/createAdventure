from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfTrips, Trip

urlpatterns = [
    path(r'trips/', listOfTrips.as_view()),
    path(r'trips/<int:pk>/', Trip.as_view()),
    # path(r'trips/', login_required(listOfTrips.as_view())),
    # path(r'trips/<int:pk>/', login_required(Trip.as_view())),
    # path(r'trips/<int:pk>/countries/', login_required(AllOfCountriesInTrip.as_view())),
    # path(r'trips/<int:trip_pk>/countries/<int:country_pk>/', login_required(particularCountryInTrip.as_view())),
]
