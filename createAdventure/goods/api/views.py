from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from requests import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Item as ItemModel
from .serializer import ItemSerializer
from rest_framework import generics, status
import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework.decorators import permission_classes


class GoodsSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'title',
                    required=True,
                ),
                coreapi.Field(
                    'price',
                    required=True,
                    type='number',
                ),
                coreapi.Field(
                    'seller',
                    required=True,
                ),
                coreapi.Field(
                    'state',
                    required=True,
                    type='integer',
                ),
                coreapi.Field(
                    'description',
                    required=True,
                ),
                coreapi.Field(
                    'type_of_item',
                    required=True,
                    type='integer',
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class listOfGoods(APIView):
    """
    List all items or Create a new item
    """

    permission_classes = [IsAuthenticated]

    schema = GoodsSchema()

    def get(self, request):
        user = request.user
        if user.is_staff:
            items = ItemModel.objects.all()
            if items.count() > 0:
                serializer = ItemSerializer(items, many=True)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
        else:
            return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

    def post(self, request):
        account = request.user
        item = ItemModel(author=account)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Item(APIView):
    """
        Retrieve, update or delete a item instance.
    """
    permission_classes = [IsAuthenticated]

    schema = GoodsSchema()

    def get(self, request, pk):
        try:
            item = ItemModel.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except ItemModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def put(self, request, pk):
        try:
            item = ItemModel.objects.get(pk=pk)

            user = request.user
            if user.is_staff:
                serializer = ItemSerializer(item, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif item.author == user:
                serializer = ItemSerializer(item, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            if item.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except ItemModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

    def delete(self, request, pk):
        try:
            item = ItemModel.objects.get(pk=pk)

            user = request.user
            if user.is_staff:
                item.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            elif item.author == user:
                item.delete()
                return JsonResponse(204, status=status.HTTP_204_NO_CONTENT, safe=False)
            if item.author != user:
                return JsonResponse(401, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        except ItemModel.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)
