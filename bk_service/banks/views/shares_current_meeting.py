# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Share, Meeting

# Serializers
from bk_service.banks.serializers import SharesModelSerializer


class ShareCurrentMeetingAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        shares = Share.objects.filter(is_active=True, meeting=None)
        serializer = SharesModelSerializer(shares, many=True)

        last_cash_balance = self.get_last_cash_balance(bank=partner.bank)
        total_quantity_shares_meeting = sum(share['quantity'] for share in serializer.data)
        total_amount_shares_meeting = sum(share['amount'] for share in serializer.data)

        res = {
            'last_cash_balance': last_cash_balance,
            'total_quantity_shares_meeting': total_quantity_shares_meeting,
            'new_cash_balance': float(last_cash_balance) + float(total_amount_shares_meeting),
            'shares_by_partners': serializer.data
        }

        return Response(res)

    def get_last_cash_balance(self, bank):
        last_meeting = bank.get_last_meeting()

        if last_meeting is not None:
            return last_meeting.cash_balance

        return 0.0
