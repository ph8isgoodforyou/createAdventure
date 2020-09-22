from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Transport as TransportModel
from .serializer import TransportSerializer
from rest_framework import generics, status

class listOfTransports(APIView):
    """
    List all Transports, or create a new Transport.
    """

    def get(self, request, format=None):
        transports = TransportModel.objects.all()
        if transports.count() > 0:
            serializer = TransportSerializer(transports, many=True)
            return JsonResponse(serializer.data, safe=False)
        else: return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Transport(APIView):
    """
    Retrieve, update or delete a Transport instance.
    """

    def get_object(self, pk):
        try:
            return TransportModel.objects.get(pk=pk)
        except TransportModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transport = self.get_object(pk)
        serializer = TransportSerializer(transport)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        transport = self.get_object(pk)
        serializer = TransportSerializer(transport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transport = self.get_object(pk)
        transport.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
