""" Appovals views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from bk_service.banks.serializers import AppovalsSerializer


class ApprovalsAPIView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = AppovalsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        partner = request.user.get_partner()

        serializer.create(partner=partner, **validated_data)

        return Response(f'share {validated_data["approval_status"]} success !')
