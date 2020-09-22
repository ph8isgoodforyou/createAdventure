from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Trip as TripModel
from .serializer import TripSerializer
from rest_framework import generics, status

import coreapi
from rest_framework.schemas import AutoSchema

class TripSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'trip_type',
                    required=True
                ),
                coreapi.Field(
                    'overall_price',
                    required=True
                ),
                coreapi.Field(
                    'list_of_items',
                    required=True
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfTrips(APIView):
    """
    List all trips, or create a new trip.
    """

    schema = TripSchema()

    def get(self, request, format=None):
        trips = TripModel.objects.all()
        if trips.count() > 0:
            serializer = TripSerializer(trips, many=True)
            return JsonResponse(serializer.data, safe=False)
        else: return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Trip(APIView):
    """
    Retrieve, update or delete a trip instance.
    """

    schema = TripSchema()

    def get_object(self, pk):
        try:
            return TripModel.objects.get(pk=pk)
        except TripModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trip = self.get_object(pk)
        trip.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
