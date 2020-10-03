from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

import coreapi
from rest_framework.schemas import AutoSchema

from .api.views import Item, listOfGoods


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


urlpatterns = [
    path(r'goods/', listOfGoods.as_view()),
    path(r'goods/<int:pk>/', Item.as_view()),
    # path(r'goods/', login_required(listOfGoods.as_view())),
    # path(r'goods/<int:pk>/', login_required(Item.as_view())),
]
