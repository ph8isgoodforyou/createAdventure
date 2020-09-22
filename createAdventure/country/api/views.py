from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Country as CountryModel
from .serializer import CountrySerializer
from rest_framework import generics, status

import coreapi
from rest_framework.schemas import AutoSchema

class CountrySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'name',
                    required=True
                ),
                coreapi.Field(
                    'population',
                    required=True
                ),
                coreapi.Field(
                    'largest_city',
                    required=True
                ),
                coreapi.Field(
                    'religion',
                    required=True
                ),
                coreapi.Field(
                    'currency',
                    required=True
                ),
                coreapi.Field(
                    'time_zone',
                    required=True
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfCountries(APIView):
    """
    List all countries, or create a new country.
    """

    schema = CountrySchema()

    def get(self, request, format=None):
        countries = CountryModel.objects.all()
        if countries.count() > 0:
            serializer = CountrySerializer(countries, many=True)
            return JsonResponse(serializer.data, safe=False)
        else: return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Country(APIView):
    """
    Retrieve, update or delete a country instance.
    """

    schema = CountrySchema()

    def get_object(self, pk):
        try:
            return CountryModel.objects.get(pk=pk)
        except CountryModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country = self.get_object(pk)
        country.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
