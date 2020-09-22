from django.contrib import admin
from django.urls import path, include
from .api.views import listOfTransports, Transport


urlpatterns = [
    path(r'transports/', listOfTransports.as_view()),
    path(r'transports/<int:pk>/', Transport.as_view()),


]
