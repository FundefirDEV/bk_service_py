""" profile views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializer
from bk_service.banks.serializers import PartnerDetailModelSerializer

# Models
from bk_service.locations.models import Country


class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()

        # TODO this is temporal
        try:
            country = partner.user.city.state.country
        except:
            country = Country.objects.first()

        country_data = {
            'id': country.id,
            'name': country.name,
            'code': country.code,
        }

        serializer = PartnerDetailModelSerializer(partner.partner_detail())

        data = serializer.data
        data['country'] = country_data

        return Response(data)
