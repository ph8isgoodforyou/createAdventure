from django.db import models
from enum import IntEnum


# Create your models here.
class AccommodationTypes(IntEnum):
    Hotel = 1
    Hostel = 2
    Motel = 3
    Cottage = 4
    Mansion = 5
    Resort = 6
    Apartment = 7
    BandB = 8
    Tent = 9
    Yacht = 10

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class RatingTypes(IntEnum):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Accommodation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    room = models.IntegerField()
    accommodation_type = models.IntegerField(choices=AccommodationTypes.choices(), default=AccommodationTypes.Hotel)
    price = models.FloatField(max_length=100)
    rating = models.IntegerField(choices=RatingTypes.choices(), default=RatingTypes.FIVE_STAR)
    date = models.DateField()
