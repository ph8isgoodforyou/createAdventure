from django.db import models
import accommodation.api.models
import goods.api.models
import placeToEat.api.models
import pointOfInterest.api.models
import transport.api.models


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    fk_accommodation = models.ForeignKey(accommodation.api.models.Accommodation, on_delete=models.CASCADE)
    fk_placeToEat = models.ForeignKey(placeToEat.api.models.PlaceToEat, on_delete=models.CASCADE)
    fk_pointOfInterest = models.ForeignKey(pointOfInterest.api.models.PointOfInterest, on_delete=models.CASCADE)
    fk_transport = models.ForeignKey(transport.api.models.Transport, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    largest_city = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=50)
