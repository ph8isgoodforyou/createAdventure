from django.contrib import admin
from django.urls import path, include
from .api.views import listOfPlacesToEat, placeToEat

urlpatterns = [
    path(r'placesToEat/', listOfPlacesToEat.as_view()),
    path(r'placesToEat/<int:pk>/', placeToEat.as_view()),
]
