from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    seller = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


    def __str__(self):
        return self.name

