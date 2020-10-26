from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'seller', 'state', 'description', 'type_of_item']
        # fields = '__all__'
