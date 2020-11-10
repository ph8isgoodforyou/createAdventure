"""createAdventure URL Configuration
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import request
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Create Adventure API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'docs/', schema_view, name='swagger'),


    path('', include('user.urls')),
    path('', include('accommodation.urls')),
    path('', include('country.urls')),
    path('', include('goods.urls')),
    path('', include('placeToEat.urls')),
    path('', include('pointOfInterest.urls')),
    path('', include('transport.urls')),
    path('', include('trip.urls')),
]
