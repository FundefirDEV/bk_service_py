# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Credit

# Serializers
from bk_service.banks.serializers import CreditsModelSerializer


class MyBankInfoAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        credits = Credit.objects.filter(partner=partner, is_active=True)
        serializer = CreditsModelSerializer(credits, many=True)

        return Response(serializer.data)
