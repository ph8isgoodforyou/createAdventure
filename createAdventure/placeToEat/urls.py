from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfPlacesToEat, placeToEat

urlpatterns = [
    path(r'placesToEat/', listOfPlacesToEat.as_view()),
    path(r'placesToEat/<int:pk>/', placeToEat.as_view()),
    # path(r'placesToEat/', login_required(listOfPlacesToEat.as_view())),
    # path(r'placesToEat/<int:pk>/', login_required(placeToEat.as_view())),
]
