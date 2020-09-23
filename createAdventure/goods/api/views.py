from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Item as ItemModel
from .serializer import ItemSerializer
from rest_framework import generics, status
import coreapi
from rest_framework.schemas import AutoSchema


class GoodsSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'name',
                    required=True,
                ),
                coreapi.Field(
                    'price',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'seller',
                    required=True,
                ),
                coreapi.Field(
                    'state',
                    required=True,
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class listOfGoods(APIView):
    """
    List all items, or create a new item.
    """
    schema = GoodsSchema()

    def get(self, request, format=None):
        items = ItemModel.objects.all()
        if items.count() > 0:
            serializer = ItemSerializer(items, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Item(APIView):
    """
        Retrieve, update or delete a item instance.
    """
    schema = GoodsSchema()

    def get_object(self, pk):
        try:
            return ItemModel.objects.get(pk=pk)
        except ItemModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return JsonResponse('HTTP_204_NO_CONTENT', safe=False)
