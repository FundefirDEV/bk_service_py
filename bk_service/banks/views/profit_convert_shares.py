""" Profit convert shares views. """

# Python
from itertools import groupby
# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Partner, EarningShare

# Serializer
from bk_service.banks.serializers import EarningShareModelSerializer
from bk_service.banks.serializers.earning_shares import ProfitPaymentSerializer
from bk_service.utils.enums.banks import PartnerType

# Errors
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *


class ProfitConvertSharesAPIView(APIView):

    def post(self, request, *args, **kwargs):

        partner = request.user.get_partner()

        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)

        data = request.data

        serializer = ProfitPaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        partner_id = validated_data['partner_id']
        bank = request.user.get_partner().bank

        earning_shares_ids = validated_data['earning_shares_ids']
        quantity = validated_data['quantity']

        serializer.convert_shares(bank, partner_id, earning_shares_ids, quantity)

        return Response('profits convert shares success')
