from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfTrips, Trip

urlpatterns = [
    path(r'trips/', login_required(listOfTrips.as_view())),
    path(r'trips/<int:pk>/', login_required(Trip.as_view())),
]
