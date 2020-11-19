from django.db import models
from django_enumfield import enum

# PointOfInterestModel  CityModel TripModel CountryModel
from rest_framework.settings import api_settings

from createAdventure import settings

class TripTypes(enum.Enum):
    The_Weekend_Break = 1
    The_Group_Tour = 2
    Road_Trip = 3
    Volunteer_Travel = 4
    The_Gap_Year = 5
    Business_Travel = 6
    Other = 7

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length= 200, null=False, blank=False)
    trip_type = enum.EnumField(TripTypes, default=TripTypes.The_Weekend_Break)
    # countries = models.ManyToManyField('country.Country', related_name='countries', blank=True)
    date_published = models.DateField(auto_now_add=True, verbose_name="date published")
    time_published = models.TimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateField(auto_now=True, verbose_name="date updated")
    time_updated = models.TimeField(auto_now=True, verbose_name="date updated")
    trip_overall_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    population = models.IntegerField()
    religion = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=50)
    trip = models.ForeignKey(Trip, related_name='countries', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class City(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    population = models.IntegerField()
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class PointOfInterest(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, related_name='pointsOfInterest', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    work_hours = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
