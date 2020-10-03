from django.db import models
from country.api.models import Country
from enum import IntEnum

class TripTypes(IntEnum):
    The_Weekend_Break = 1
    The_Package_Holiday = 2
    The_Group_Tour = 3
    Road_Trip = 4
    Volunteer_Travel = 5
    The_Gap_Year = 6
    Event_Travel = 7
    Business_Travel = 8


    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

# Create your models here.
class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    # fk_country = models.ForeignKey(CountryModel, related_name='countries', on_delete=models.CASCADE)
    trip_type = models.IntegerField(choices=TripTypes.choices(), default=TripTypes.The_Weekend_Break)
    overall_price = models.FloatField(max_length=10000000)
    list_of_items = models.CharField(max_length=1000)
    countries = models.ManyToManyField('country.Country', related_name='countries', blank=True)
    # listi = models.ExpressionList()