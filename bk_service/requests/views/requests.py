""" Request views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from bk_service.requests.serializers import RequestsSerializer


class RequestsAPIView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = RequestsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        return Response('manaos')
