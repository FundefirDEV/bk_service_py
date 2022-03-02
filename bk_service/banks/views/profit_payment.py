""" Profit payment views. """

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


class ProfitPaymentAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner_id = kwargs['partner_id']
        bank = request.user.get_partner().bank
        partner = get_object_or_404(Partner, pk=partner_id, bank=bank)
        earning_shares = EarningShare.objects.filter(share__partner=partner)
        earning_share_serializer = EarningShareModelSerializer(earning_shares, many=True)

        total_earning = partner.partner_detail().earnings + partner.partner_detail().profit_obtained

        res = {
            'total_earning': total_earning,
            'earning_shares': earning_share_serializer.data
        }

        return Response(res)

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

        serializer.pay_earnings_shares(bank, partner_id, earning_shares_ids)

        return Response('profits payment success')
