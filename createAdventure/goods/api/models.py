from enum import IntEnum

from django.db import models

class ItemState(IntEnum):
    New = 1
    Used = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class ItemType(IntEnum):
    Unspecified = 1
    Clothing = 2
    Shoes = 3
    Glasses = 4
    Backpacks = 5
    Camping_Gear = 6
    Tools = 7
    Lights = 8
    Watches = 9

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    seller = models.CharField(max_length=100)
    state = models.IntegerField(choices=ItemState.choices(), default=ItemState.New)
    description = models.CharField(max_length=500)
    type_of_item = models.IntegerField(choices=ItemType.choices(), default=ItemType.Unspecified)



