from rest_framework import serializers
from .models import PointOfInterest


class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        fields = [
            'id',
            'name',
            'price_to_visit',
            'images_links',
            'rating',
            'address',
        ]