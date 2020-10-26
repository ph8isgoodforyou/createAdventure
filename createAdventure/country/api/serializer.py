from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Country
        fields = [
            'id',
            'name',
            'population',
            'largest_city',
            'religion',
            'currency',
            'time_zone',
        ]
        # extra_kwargs = {'trips': {'required': False}}