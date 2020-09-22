from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Item as ItemModel
from .serializer import ItemSerializer
from rest_framework import generics, status

class listOfGoods(APIView):
    """
    List all items, or create a new item.
    """

    def get(self, request, format=None):
        items = ItemModel.objects.all()
        if items.count() > 0:
            serializer = ItemSerializer(items, many=True)
            return JsonResponse(serializer.data, safe=False)
        else: return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Item(APIView):
    """
    Retrieve, update or delete a item instance.
    """

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
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

