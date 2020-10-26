from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView, TemplateView

from account.api.views import (
    registration_view_API,
    update_token_view_API
)

app_name = "account"

urlpatterns = [
    # path('register', registration_view_API, name="register"),
    # path('login', obtain_auth_token, name="login"),
    # path('token/<int:pk>/', update_token_view_API, name="updateToken"),
]
