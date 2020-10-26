from django.http import JsonResponse
from django.template.defaulttags import csrf_token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
import coreapi
from rest_framework.schemas import AutoSchema
from account.api.serializer import RegistrationSerializer

class AccountSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(
                    'email',
                    required=True,
                ),
                coreapi.Field(
                    'username',
                    required=True,
                ),
                coreapi.Field(
                    'password',
                    required=True,
                ),
                coreapi.Field(
                    'password2',
                    required=True,
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class RegisterAccount(APIView):

    permission_classes = []

    schema = AccountSchema()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        else:
            # data = serializer.errors
            return JsonResponse(400, status=status.HTTP_400_BAD_REQUEST, safe=False)

class UpdateAccountToken(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            data = {}
            data['oldToken'] = Token.objects.get(user=pk).key
            token = Token.objects.filter(user=pk)
            new_key = token[0].generate_key()
            token.update(key=new_key)
            data['newToken'] = Token.objects.get(user=pk).key
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except Token.DoesNotExist:
            return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)

# @api_view(['POST', ])
# def registration_view_API(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#             data['response'] = 'successfully registered new user.'
#             data['email'] = account.email
#             data['username'] = account.username
#             token = Token.objects.get(user=account).key
#             data['token'] = token
#             return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
#         else:
#             # data = serializer.errors
#             return JsonResponse(400, status=status.HTTP_400_BAD_REQUEST, safe=False)
#         # return Response(data)
#
# @api_view(['PUT', ])
# def update_token_view_API(request, pk):
#     try:
#         data = {}
#         data['oldToken'] = Token.objects.get(user=pk).key
#         token = Token.objects.filter(user=pk)
#         new_key = token[0].generate_key()
#         token.update(key=new_key)
#         data['newToken'] = Token.objects.get(user=pk).key
#         return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
#     except Token.DoesNotExist:
#         return JsonResponse(404, status=status.HTTP_404_NOT_FOUND, safe=False)