from rest_framework import serializers
from .models import Trip
from country.api.serializer import CountrySerializer


class TripSerializer(serializers.ModelSerializer):
    # countries = CountrySerializer(many=True)

    class Meta:
        model = Trip
        fields = [
            'id',
            'trip_type',
            'overall_price',
            'list_of_items',
        ]


    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['countries'] = TripSerializer(instance.countries).data
    #     return ret