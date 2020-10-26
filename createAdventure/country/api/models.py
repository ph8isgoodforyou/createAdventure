from django.db import models
import accommodation.api.models
import placeToEat.api.models
import pointOfInterest.api.models
import transport.api.models
from django.conf import settings


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    largest_city = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
