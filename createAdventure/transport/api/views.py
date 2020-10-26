from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Transport as TransportModel
from .serializer import TransportSerializer
from rest_framework import generics, status

import coreapi
from rest_framework.schemas import AutoSchema

class TransportSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'transportation_type',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'name',
                    required=True
                ),
                coreapi.Field(
                    'price',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'date_available',
                    required=True
                ),
                coreapi.Field(
                    'address',
                    required=True
                ),
                coreapi.Field(
                    'link',
                    required=True
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfTransports(APIView):
    """
    List all Transports, or create a new Transport.
    """
    permission_classes = [IsAuthenticated]

    schema = TransportSchema()

    def get(self, request):
        user = request.user
        if user.is_staff:
            transports = TransportModel.objects.all()
            if transports.count() > 0:
                serializer = TransportSerializer(transports, many=True)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def post(self, request):
        user = request.user
        if user.is_staff:

            account = request.user
            transport = TransportModel(author=account)

            serializer = TransportSerializer(transport, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

class Transport(APIView):
    """
    Retrieve, update or delete a Transport instance.
    """

    permission_classes = [IsAuthenticated]

    schema = TransportSchema()

    def get(self, request, pk):
        try:
            transport = TransportModel.objects.get(pk=pk)
            serializer = TransportSerializer(transport)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except TransportModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                transport = TransportModel.objects.get(pk=pk)

                # user = request.user
                # if transport.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                serializer = TransportSerializer(transport, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except TransportModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def delete(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                transport = TransportModel.objects.get(pk=pk)

                # user = request.user
                # if transport.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                transport.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            except TransportModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)