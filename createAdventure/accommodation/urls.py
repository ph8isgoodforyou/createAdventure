from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfAccommodations, Accommodation


urlpatterns = [
    path(r'accommodations/', listOfAccommodations.as_view()),
    path(r'accommodations/<int:pk>/', Accommodation.as_view()),
    # path(r'accommodations/', login_required(listOfAccommodations.as_view())),
    # path(r'accommodations/<int:pk>/', login_required(Accommodation.as_view())),
]
