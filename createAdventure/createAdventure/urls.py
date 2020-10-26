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

# from account.views import (
#     registration_view,
# )
from account.views import (
    registration_view,
    logout_view,
    login_view,
)

schema_view = get_swagger_view(title='Create Adventure API Documentation')

urlpatterns = [
    # url('/', home, name="home"),
    # url('login/', login_view, name="login"),
    # url('logout/', logout_view, name="logout"),
    # url('register/', registration_view, name="register"),

    path('admin/', admin.site.urls),

    url(r'docs/', schema_view, name='swagger'),
    # path('', login_required(schema_view), name='swagger'),
    # path('', include('account.api.urls')),
    path('', include('account.urls')),
    path('', include('accommodation.urls')),
    path('', include('country.urls')),
    path('', include('goods.urls')),
    path('', include('placeToEat.urls')),
    path('', include('pointOfInterest.urls')),
    path('', include('transport.urls')),
    path('', include('trip.urls')),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
            allauth provided urls
--------------------------------------------------------
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("password/change/", views.password_change,
         name="account_change_password"),
    path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", views.account_inactive, name="account_inactive"),

    # E-mail
    path("email/", views.email, name="account_email"),
    path("confirm-email/", views.email_verification_sent,
         name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
            name="account_confirm_email"),

    # password reset
    path("password/reset/", views.password_reset,
         name="account_reset_password"),
    path("password/reset/done/", views.password_reset_done,
         name="account_reset_password_done"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            views.password_reset_from_key,
            name="account_reset_password_from_key"),
    path("password/reset/key/done/", views.password_reset_from_key_done,
         name="account_reset_password_from_key_done"),
"""
