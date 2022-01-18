""" Meeting views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# bk_core
from bk_service.bk_core_sdk import BkCoreSDK

# Serializers

# bk_core
from bk_service.bk_core_sdk.bk_core import BkCore


class MeetingsGetAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        partner_detail = partner.partner_detail()
        bank = partner.bank

        bk_core_sdk = BkCoreSDK(partner=partner)

        res = bk_core_sdk.create_meeting(preview=True)

        return Response(res)
