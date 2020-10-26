from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView, TemplateView

from account.api.views import (
    RegisterAccount,
    UpdateAccountToken,
)

app_name = "account"

urlpatterns = [
    path('register', RegisterAccount.as_view()),
    path('token/<int:pk>/', UpdateAccountToken.as_view()),
]
