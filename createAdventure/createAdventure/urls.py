"""createAdventure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Create Adventure API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'docs/', schema_view, name='swagger'),
    path('', schema_view, name='swagger'),
    path('', include('accommodation.urls')),
    path('', include('country.urls')),
    path('', include('goods.urls')),
    path('', include('placeToEat.urls')),
    path('', include('pointOfInterest.urls')),
    path('', include('transport.urls')),
    path('', include('trip.urls')),
]