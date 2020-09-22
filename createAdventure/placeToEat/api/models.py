from enum import IntEnum
from django.db import models


class RatingTypes(IntEnum):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class InstitutionTypes(IntEnum):
    Ethnic = 1
    FastFood = 2
    Pub = 3
    Cafe = 4
    Restaurant = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


# Create your models here.
class PlaceToEat(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    institution_type = models.IntegerField(choices=InstitutionTypes.choices(), default=InstitutionTypes.Restaurant)
    rating = models.IntegerField(choices=RatingTypes.choices(), default=RatingTypes.FIVE_STAR)
