from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Country
        fields = '__all__'
        # extra_kwargs = {'trips': {'required': False}}
