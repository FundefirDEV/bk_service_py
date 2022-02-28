""" Profit payment views. """

# Python
from itertools import groupby
# Django
from django.shortcuts import get_object_or_404
from django.db.models.functions import TruncYear, TruncMonth
from django.db.models import Count

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Partner, EarningShare

# Serializer
from bk_service.banks.serializers import EarningShareModelSerializer


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
