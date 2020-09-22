from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Accommodation as AccommodationModel
from .serializer import AccommodationSerializer
from rest_framework import  status

class listOfAccommodations(APIView):
    """
    List all accommodations, or create a new accommodation.
    """

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

