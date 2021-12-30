""" Delete partner guest view. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models.partners_guest import PartnerGuest

# Utils
from bk_service.utils.exceptions_errors import CustomValidation
from bk_service.utils.constants_errors import PARTNER_GUEST_NOT_EXIST

import pdb


class DeletePartnerGuestAPIView(APIView):

    def post(self, request, *args, **kwargs):

        phone = request.data
        try:
            partner_guest = PartnerGuest.objects.get(phone_number=phone)
            partner_guest.delete()
            return Response('partner guest was deleted')
        except:
            raise CustomValidation(error=PARTNER_GUEST_NOT_EXIST)
