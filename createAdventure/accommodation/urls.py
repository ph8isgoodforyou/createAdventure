from django.contrib import admin
from django.urls import path, include
from .api.views import listOfAccommodations, Accommodation


urlpatterns = [
    path(r'accommodations/', listOfAccommodations.as_view()),
    path(r'accommodations/<int:pk>/', Accommodation.as_view()),
]
