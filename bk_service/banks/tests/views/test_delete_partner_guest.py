""" Delete partner guest test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Models
from bk_service.banks.models.partners_guest import PartnerGuest

# Utils
from bk_service.banks.tests.utils.setup import create_partner, invite_partner

# Utils commons
from bk_service.utils.tests.requests import post_with_token

# error
from bk_service.utils.constants_errors import build_error_message, PARTNER_GUEST_NOT_EXIST


# import pdb
# pdb.set_trace()

URL = '/banks/delete-partner-guest/'


class DeletePartnerGuestTestCase(APITestCase):
    """delete partner guest test class """

    def setUp(self):
        partner = create_partner()
        self.user = partner.user
        invite_partner(bank=partner.bank, phone_number='30000000')

    def test_delete_partner_guest(self):
        """ delete partner guest success """

        body = '30000000'
        request = post_with_token(URL, user=self.user, body=body,)
        body = request.data

        partner_guest = PartnerGuest.objects.filter(phone_number='30000000')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'partner guest was deleted')
        self.assertEqual(len(partner_guest), 0)

    def test_delete_partner_guest(self):
        """ delete partner guest success """

        body = '30000001'
        request = post_with_token(URL, user=self.user, body=body,)
        body = request.data

        partner_guest = PartnerGuest.objects.filter(phone_number='30000000')

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=PARTNER_GUEST_NOT_EXIST)})
        self.assertEqual(len(partner_guest), 1)
