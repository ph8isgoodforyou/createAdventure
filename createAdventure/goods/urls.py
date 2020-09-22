from django.contrib import admin
from django.urls import path, include
from .api.views import listOfGoods, Item

urlpatterns = [
    path(r'goods/', listOfGoods.as_view()),
    path(r'goods/<int:pk>/', Item.as_view()),
]
