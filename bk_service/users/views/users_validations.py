""" User validations views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Serializers
from bk_service.users.serializers import (EmailExistSerializer)


class VerifyEmail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.data
        serializer = EmailExistSerializer(data=data)
        return Response('ok')
