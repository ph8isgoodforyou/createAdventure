from enum import IntEnum
from django.db import models
from django.conf import settings

import country


class TransportationTypes(IntEnum):
    Plane = 1
    Ship = 2
    Bus = 3
    Train = 4
    Car = 5
    ByFoot = 6
    Bicycle = 7

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


# Create your models here.
class Transport(models.Model):
    id = models.AutoField(primary_key=True)
    transportation_type = models.IntegerField(choices=TransportationTypes.choices(), default=TransportationTypes.Plane)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    date_available =models.DateField()
    address = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    # fk_country = models.ForeignKey(country.api.models.Country, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
