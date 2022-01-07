""" Partners views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

from bk_service.banks.models.partners import Partner


class PartnerAPIView(APIView):
    def get(self, request, *args, **kwargs):

        bank = request.user.get_partner().bank

        partners = Partner.objects.filter(bank=bank)
        response = []

        for partner in partners:
            response.append({'id': partner.id,
                             'phone': partner.phone_number,
                             'is_active': partner.is_active,
                             'role': partner.role})

        return Response(response)
