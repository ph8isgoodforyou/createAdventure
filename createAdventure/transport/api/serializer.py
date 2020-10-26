from rest_framework import serializers
from .models import Transport


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = [
            'id',
            'transportation_type',
            'name',
            'price',
            'date_available',
            'address',
            'link',
        ]
