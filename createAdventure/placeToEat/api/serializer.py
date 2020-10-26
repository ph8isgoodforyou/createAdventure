from rest_framework import serializers
from .models import PlaceToEat


class PlaceToEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceToEat
        fields = [
            'id',
            'title',
            'institution_type',
            'rating',
        ]
