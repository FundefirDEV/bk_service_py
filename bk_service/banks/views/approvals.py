""" Appovals views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from bk_service.banks.serializers import AppovalsSerializer

# Utils enums
from bk_service.utils.enums.banks import PartnerType

# Errors
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *


class ApprovalsAPIView(APIView):

    def post(self, request, *args, **kwargs):

        partner = request.user.get_partner()

        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        data = request.data
        serializer = AppovalsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        serializer.create(partner=partner, **validated_data)

        return Response(f'share {validated_data["approval_status"]} success !')


CustomException
