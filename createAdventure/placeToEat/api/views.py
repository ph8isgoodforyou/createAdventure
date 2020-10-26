from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import PlaceToEat as PlaceToEatModel
from .serializer import PlaceToEatSerializer
from rest_framework import generics, status

import coreapi
from rest_framework.schemas import AutoSchema

class PlaceToEatSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'title',
                    required=True
                ),
                coreapi.Field(
                    'institution_type',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'rating',
                    required=True,
                    type='integer',
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class listOfPlacesToEat(APIView):
    """
    List all placesToEat, or create a new placeToEat.
    """

    permission_classes = [IsAuthenticated]

    schema = PlaceToEatSchema()

    def get(self, request):
        user = request.user
        if user.is_staff:
            placesToEat = PlaceToEatModel.objects.all()
            if placesToEat.count() > 0:
                serializer = PlaceToEatSerializer(placesToEat, many=True)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def post(self, request):
        user = request.user
        if user.is_staff:

            account = request.user
            placesToEat = PlaceToEatModel(author=account)

            serializer = PlaceToEatSerializer(placesToEat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

class placeToEat(APIView):
    """
    Retrieve, update or delete a placeToEat instance.
    """

    permission_classes = [IsAuthenticated]

    schema = PlaceToEatSchema()

    def get(self, request, pk):
        try:
            placeToEat = self.get_object(pk)
            serializer = PlaceToEatSerializer(placeToEat)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                placeToEat = self.get_object(pk)

                # user = request.user
                # if placeToEat.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                serializer = PlaceToEatSerializer(placeToEat, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except PlaceToEatModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def delete(self, request, pk):
        user = request.user
        if user.is_staff:
            try:
                placeToEat = PlaceToEatModel.objects.get(pk=pk)

                # user = request.user
                # if placeToEat.author != user:
                #     return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

                placeToEat.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            except PlaceToEatModel.DoesNotExist:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)