""" Delete partner guest view. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models.partners_guest import PartnerGuest

# Serializers
from bk_service.banks.serializers.partners_guest import PartnersGuestSerializer

# Utils
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import PARTNER_GUEST_NOT_EXIST

# import pdb


class DeletePartnerGuestAPIView(APIView):

    def post(self, request, *args, **kwargs):

        phone = request.data
        try:
            partner_guest = PartnerGuest.objects.get(phone_number=phone)
            partner_guest.delete()
            return Response('partner guest was deleted')
        except:
            raise CustomException(error=PARTNER_GUEST_NOT_EXIST)


class InvitePartnerGuestAPIView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        bank = request.user.get_partner().bank

        data['bank'] = bank.id

        serializer = PartnersGuestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        serializer.create(validated_data=validated_data,)

        return Response('partner guest was created')
