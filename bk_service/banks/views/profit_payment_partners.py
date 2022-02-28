""" Profit payment partners views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models.partner_details import PartnerDetail

# Serializer
from bk_service.banks.serializers import PartnerDetailModelSerializer


class ProfitPaymentPartnersAPIView(APIView):
    def get(self, request, *args, **kwargs):

        bank = request.user.get_partner().bank

        partners_detail = PartnerDetail.objects.filter(partner__bank=bank, partner__is_active=True)

        serializer = PartnerDetailModelSerializer(partners_detail, many=True)

        total_profit_obtained = sum(p['profit_obtained'] for p in serializer.data)

        res = {
            'partners': serializer.data,
            'total_profit_obtained': total_profit_obtained
        }

        return Response(res)
