from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import PlaceToEat as PlaceToEatModel
from .serializer import PlaceToEatSerializer
from rest_framework import generics, status

class listOfPlacesToEat(APIView):
    """
    List all placesToEat, or create a new placeToEat.
    """

    def get(self, request, format=None):
        placesToEat = PlaceToEatModel.objects.all()
        if placesToEat.count() > 0:
            serializer = PlaceToEatSerializer(placesToEat, many=True)
            return JsonResponse(serializer.data, safe=False)
        else: return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = PlaceToEatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class placeToEat(APIView):
    """
    Retrieve, update or delete a placeToEat instance.
    """

    def get_object(self, pk):
        try:
            return PlaceToEatModel.objects.get(pk=pk)
        except PlaceToEatModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        placeToEat = self.get_object(pk)
        serializer = PlaceToEatSerializer(placeToEat)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        placeToEat = self.get_object(pk)
        serializer = PlaceToEatSerializer(placeToEat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        placeToEat = self.get_object(pk)
        placeToEat.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
