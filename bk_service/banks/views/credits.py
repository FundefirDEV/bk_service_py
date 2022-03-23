# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Credit

# Serializers
from bk_service.banks.serializers import CreditsModelSerializer


class CreditModelAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        credit = Credit.objects.filter(is_active=True, bank=partner.bank, partner=partner)
        serializer = CreditsModelSerializer(credit, many=True)

        return Response(serializer.data)
