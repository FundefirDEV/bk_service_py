""" User validations views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Serializers
from bk_service.banks.serializers.partners import PartnerPhoneExistSerializer, PartnerGuestPhoneExistSerializer


class VerifyPartnerPhone(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        serializer = PartnerPhoneExistSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)

        return Response('phone is valid')


class VerifyPartnerGuestPhone(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        serializer = PartnerGuestPhoneExistSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)

        return Response('phone is valid')
