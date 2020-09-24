from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfGoods, Item

urlpatterns = [
    path(r'goods/', login_required(listOfGoods.as_view())),
    path(r'goods/<int:pk>/', login_required(Item.as_view())),
]
