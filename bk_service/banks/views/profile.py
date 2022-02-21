""" profile views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializer
from bk_service.banks.serializers import PartnerDetailModelSerializer


class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()

        serializer = PartnerDetailModelSerializer(partner.partner_detail())

        return Response(serializer.data)
