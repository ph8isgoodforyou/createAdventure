from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfPointsOfInterest, pointOfInterest

urlpatterns = [
    path(r'pointsOfInterest/', listOfPointsOfInterest.as_view()),
    path(r'pointsOfInterest/<int:pk>/', pointOfInterest.as_view()),
    # path(r'pointsOfInterest/', login_required(listOfPointsOfInterest.as_view())),
    # path(r'pointsOfInterest/<int:pk>/', login_required(pointOfInterest.as_view())),
]
