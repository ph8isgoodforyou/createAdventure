from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Accommodation as AccommodationModel
from .serializer import AccommodationSerializer
from rest_framework import  status

import coreapi
from rest_framework.schemas import AutoSchema

class AccommodationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'title',
                    required=True
                ),
                coreapi.Field(
                    'address',
                    required=True
                ),
                coreapi.Field(
                    'room',
                    required=True
                ),
                coreapi.Field(
                    'accommodation_type',
                    required=True
                ),
                coreapi.Field(
                    'price',
                    required=True
                ),
                coreapi.Field(
                    'date',
                    required=True
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfAccommodations(APIView):
    """
    List all accommodations, or create a new accommodation.
    """

    schema = AccommodationSchema()

    def get(self, request, format=None):
        accommodation = AccommodationModel.objects.all()
        if accommodation.count() > 0:
            serializer = AccommodationSerializer(accommodation, many=True)
            return JsonResponse(serializer.data, safe=False)
        else: return JsonResponse('HTTP_404_NOT_FOUND', safe=False)

    def post(self, request, format=None):
        serializer = AccommodationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Accommodation(APIView):
    """
    Retrieve, update or delete a accommodation instance.
    """

    schema = AccommodationSchema()

    def get_object(self, pk):
        try:
            return AccommodationModel.objects.get(pk=pk)
        except AccommodationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        accommodation = self.get_object(pk)
        serializer = AccommodationSerializer(accommodation)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        accommodation = self.get_object(pk)
        serializer = AccommodationSerializer(accommodation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        accommodation = self.get_object(pk)
        accommodation.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

