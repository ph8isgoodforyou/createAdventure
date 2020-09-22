from django.contrib import admin
from django.urls import path, include
from .api.views import listOfTrips, Trip

urlpatterns = [
    path(r'trips/', listOfTrips.as_view()),
    path(r'trips/<int:pk>/', Trip.as_view()),
]
