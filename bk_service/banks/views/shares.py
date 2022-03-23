# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Share

# Serializers
from bk_service.banks.serializers import SharesModelSerializer


class SharesModelAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        shares = Share.objects.filter(is_active=True, bank=partner.bank, partner=partner)
        serializer = SharesModelSerializer(shares, many=True)

        return Response(serializer.data)
