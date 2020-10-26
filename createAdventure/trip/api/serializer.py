from rest_framework import serializers
from .models import Trip
from country.api.serializer import CountrySerializer


class TripSerializer(serializers.ModelSerializer):
    # countries = CountrySerializer(many=True)

    class Meta:
        model = Trip
        fields = [
            'id',
            'title',
            'trip_type',
            'overall_price',
            'list_of_items',
            'date_published',
            'date_updated',
        ]


    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['countries'] = TripSerializer(instance.countries).data
    #     return ret