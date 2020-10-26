from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .models import Country as CountryModel
from .serializer import CountrySerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import coreapi
from rest_framework.schemas import AutoSchema

class CountrySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'fk_accommodation',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'fk_placeToEat',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'fk_pointOfInterest',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'fk_transport',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'name',
                    required=True,
                ),
                coreapi.Field(
                    'population',
                    required=True,
                ),
                coreapi.Field(
                    'largest_city',
                    required=True,
                ),
                coreapi.Field(
                    'religion',
                    required=True,
                ),
                coreapi.Field(
                    'currency',
                    required=True,
                ),
                coreapi.Field(
                    'time_zone',
                    required=True,
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfCountries(APIView):
    """
    List all countries, or create a new country.
    """

    permission_classes = [IsAuthenticated]

    schema = CountrySchema()

    def get(self, request):
        user = request.user
        # update_token_view_API(request='PUT', pk=user.id)
        if user.is_staff:
            countries = CountryModel.objects.all()
            if countries.count() > 0:
                serializer = CountrySerializer(countries, many=True)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def post(self, request):
        user = request.user
        if user.is_staff:

            account = request.user
            country = CountryModel(author=account)

            serializer = CountrySerializer(country, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

class particularCountry(APIView):
    """
    Retrieve, update or delete a country instance.
    """

    permission_classes = [IsAuthenticated]

    schema = CountrySchema()

    def get(self, request, pk):
        # user = request.user
        # update_token_view_API(request, pk=user.id)
        try:
            country = CountryModel.objects.get(pk=pk)
            serializer = CountrySerializer(country)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except CountryModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                country = CountryModel.objects.get(pk=pk)

                # user = request.user
                # if country.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                serializer = CountrySerializer(country, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except CountryModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def delete(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                country = CountryModel.objects.get(pk=pk)

                # user = request.user
                # if country.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                country.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            except CountryModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)