from django.conf.urls import url
from django.urls import path, include

from .views import (
    listOfTrips,
    Trip,
    Country,
    listOfCountries,
    City,
    listOfCities,
    pointOfInterest,
    listOfPointsOfInterest,
)

urlpatterns = [
    path(r'trips/', listOfTrips.as_view()),
    path(r'trips/<int:pk>/', Trip.as_view()),
    # path(r'trips/<int:trip_pk>/countries/', Trip_Countries.as_view()),
    # path(r'trips/<int:trip_pk>/countries/<int:country_pk>/', Trip_Country.as_view()),
    # path(r'trips/<int:pk>/countries/<int:pk>/city/', Trip.as_view()),
    # path(r'trips/<int:pk>/countries/<int:pk>/city/<int:pk>/', Trip.as_view()),
    # path(r'trips/<int:pk>/countries/<int:pk>/city/<int:pk>/pointsOfInterest/', Trip.as_view()),
    # path(r'trips/<int:pk>/countries/<int:pk>/city/<int:pk>/pointsOfInterest/<int:pk>/', Trip.as_view()),
    path(r'countries/', listOfCountries.as_view()),
    path(r'countries/<int:pk>/', Country.as_view()),
    # path(r'countries/<int:pk>/city/', listOfCountries.as_view()),
    # path(r'countries/<int:pk>/city/<int:pk>/', Country.as_view()),
    # path(r'countries/<int:pk>/city/<int:pk>/pointsOfInterest/', listOfCountries.as_view()),
    # path(r'countries/<int:pk>/city/<int:pk>/pointsOfInterest/<int:pk>/', Country.as_view()),
    path(r'cities/', listOfCities.as_view()),
    path(r'cities/<int:pk>/', City.as_view()),
    # path(r'city/<int:pk>/pointsOfInterest/', City.as_view()),
    # path(r'city/<int:pk>/pointsOfInterest/<int:pk>/', City.as_view()),
    path(r'pointsOfInterest/', listOfPointsOfInterest.as_view()),
    path(r'pointsOfInterest/<int:pk>/', pointOfInterest.as_view()),
]
