""" profile views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializer
from bk_service.banks.serializers import PartnerDetailModelSerializer


class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        country = partner.user.city.state.country
        country_data = {
            'id': country.id,
            'name': country.name,
            'code': country.code,
        }

        serializer = PartnerDetailModelSerializer(partner.partner_detail())

        data = serializer.data
        data['country'] = country_data

        return Response(data)
