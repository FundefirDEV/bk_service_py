""" User validations views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Serializers
from bk_service.users.serializers import EmailExistSerializer, PhoneExistSerializer


class VerifyEmail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        serializer = EmailExistSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)

        return Response('email is valid')


class VerifyPhoneNumber(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        serializer = PhoneExistSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)

        return Response('phone is valid')
