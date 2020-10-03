from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import PointOfInterest as PointOfInterestModel
from .serializer import PointOfInterestSerializer
from rest_framework import generics, status

import coreapi
from rest_framework.schemas import AutoSchema

class PointOfInterestSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'name',
                    required=True
                ),
                coreapi.Field(
                    'price_to_visit',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'images_links',
                    required=True
                ),
                coreapi.Field(
                    'rating',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'address',
                    required=True
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfPointsOfInterest(APIView):
    """
    List all pointOfInterest, or create a new pointOfInterest.
    """

    schema = PointOfInterestSchema()

    def get(self, request):
        pointsOfInterest = PointOfInterestModel.objects.all()
        if pointsOfInterest.count() > 0:
            serializer = PointOfInterestSerializer(pointsOfInterest, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def post(self, request):
        serializer = PointOfInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class pointOfInterest(APIView):
    """
    Retrieve, update or delete a pointOfInterest instance.
    """

    schema = PointOfInterestSchema()

    def get(self, request, pk):
        try:
            pointOfInterest = PointOfInterestModel.objects.get(pk=pk)
            serializer = PointOfInterestSerializer(pointOfInterest)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except PointOfInterestModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        try:
            pointOfInterest = PointOfInterestModel.objects.get(pk=pk)
            serializer = PointOfInterestSerializer(pointOfInterest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PointOfInterestModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        try:
            pointOfInterest = PointOfInterestModel.objects.get(pk=pk)
            pointOfInterest.delete()
            return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
        except PointOfInterestModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)