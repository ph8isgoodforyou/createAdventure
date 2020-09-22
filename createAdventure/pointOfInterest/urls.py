from django.contrib import admin
from django.urls import path, include
from .api.views import listOfPointsOfInterest, pointOfInterest

urlpatterns = [
    path(r'pointsOfInterest/', listOfPointsOfInterest.as_view()),
    path(r'pointsOfInterest/<int:pk>/', pointOfInterest.as_view()),
]
