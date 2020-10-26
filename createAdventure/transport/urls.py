from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views import listOfTransports, Transport


urlpatterns = [
    path(r'transports/', listOfTransports.as_view()),
    path(r'transports/<int:pk>/', Transport.as_view()),
    # path(r'transports/', login_required(listOfTransports.as_view())),
    # path(r'transports/<int:pk>/', login_required(Transport.as_view())),


]
