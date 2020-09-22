from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ['id', 'name', 'price', 'seller', 'state']
        fields = '__all__'
