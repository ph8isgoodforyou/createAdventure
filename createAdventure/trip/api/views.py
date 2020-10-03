import coreschema
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from country.api.views import CountrySchema
from country.api.models import Country as CountryModel
from country.api.models import Country
from country.api.serializer import CountrySerializer
from .models import Trip as TripModel, Trip
from .serializer import TripSerializer
from rest_framework import generics, status, viewsets
from ast import literal_eval
import coreapi
from rest_framework.schemas import AutoSchema


class TripSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'trip_type',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'overall_price',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'list_of_items',
                    required=True
                ),
                coreapi.Field(
                    'countries',
                    required=False,

                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class TripCountrySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        schema = CountrySchema()
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'trip_type',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'overall_price',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'list_of_items',
                    required=True
                ),
                # schema,
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfTrips(APIView):
    """
    List all trips, or create a new trip.
    """

    schema = TripSchema()

    def get(self, request):
        trips = TripModel.objects.all()
        if trips.count() > 0:
            serializer = TripSerializer(trips, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            # return JsonResponse(status=status.HTTP_404_NOT_FOUND)
            return JsonResponse('HTTP_404_NOT_FOUND', safe=False)

    def post(self, request):
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

    def get(self, request, pk):
        try:
            trip = TripModel.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except TripModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        try:
            trip = TripModel.objects.get(pk=pk)
            serializer = TripSerializer(trip, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TripModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        try:
            trip = TripModel.objects.get(pk=pk)
            trip.delete()
            return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
        except TripModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)


