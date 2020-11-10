from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Accommodation as AccommodationModel
from .serializer import AccommodationSerializer
from rest_framework import status, generics

import coreapi
from rest_framework.schemas import AutoSchema


class AccommodationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'title',
                    required=True,
                ),
                coreapi.Field(
                    'address',
                    required=True,
                ),
                coreapi.Field(
                    'room',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'accommodation_type',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'price',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'rating',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'date',
                    required=True,
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class listOfAccommodations(APIView):
    """
    List all accommodations, or create a new accommodation.
    """

    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    schema = AccommodationSchema()

    def get(self, request):
        user = request.user
        if user.is_staff:
            accommodation = AccommodationModel.objects.all()
            if accommodation.count() > 0:
                serializer = AccommodationSerializer(accommodation, many=True)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def post(self, request):
        user = request.user
        if user.is_staff:

            account = request.user
            accommodation = AccommodationModel(author=account)

            serializer = AccommodationSerializer(accommodation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

class Accommodation(APIView):
    """
    Retrieve, update or delete a accommodation instance.
    """

    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    schema = AccommodationSchema()

    # def get_object(self, pk):
    #     try:
    #         return AccommodationModel.objects.get(pk=pk)
    #     except AccommodationModel.DoesNotExist:
    #         raise Http404

    def get(self, request, pk):
        try:
            accommodation = AccommodationModel.objects.get(pk=pk)

            serializer = AccommodationSerializer(accommodation)
            # update_auth_token(request.user.id)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except AccommodationModel.DoesNotExist:
            # update_auth_token(request.user.id)
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                accommodation = AccommodationModel.objects.get(pk=pk)

                # user = request.user
                # if accommodation.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                serializer = AccommodationSerializer(accommodation, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except AccommodationModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def delete(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                accommodation = AccommodationModel.objects.get(pk=pk)

                # user = request.user
                # if accommodation.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                accommodation.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            except AccommodationModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)
