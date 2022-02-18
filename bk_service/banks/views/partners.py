""" Partners views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models.partners import Partner
from bk_service.banks.models.partners_guest import PartnerGuest

from bk_service.utils.enums.banks import PartnerType


class PartnerAPIView(APIView):
    def get(self, request, *args, **kwargs):

        bank = request.user.get_partner().bank

        partners = Partner.objects.filter(bank=bank)
        partners_guests = PartnerGuest.objects.filter(bank=bank)

        partners_response = []

        for partner in partners:
            partners_response.append({'id': partner.id,
                                      'phone': partner.phone_number,
                                      'phone_region_code': partner.phone_region_code,
                                      'first_name': partner.user.first_name,
                                      'last_name': partner.user.last_name,
                                      'name':  f'{ partner.user.first_name} {partner.user.last_name}',
                                      'is_active': partner.is_active,
                                      'role': partner.role})

        for partner_guest in partners_guests:
            partners_response.append({'id': partner_guest.id,
                                      'phone': partner_guest.phone_number,
                                      'phone_region_code': partner_guest.phone_region_code,
                                      'is_active': False,
                                      'name':  partner_guest.name,
                                      'role': PartnerType.guest})

        return Response(partners_response)
