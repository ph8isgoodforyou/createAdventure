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

# Create your models here.
class PointOfInterest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price_to_visit = models.FloatField(max_length=100)
    images_links = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RatingTypes.choices(), default=RatingTypes.FIVE_STAR)
    address = models.CharField(max_length=100)

