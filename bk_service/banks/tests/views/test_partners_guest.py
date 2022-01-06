""" partner guest test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Models
from bk_service.banks.models.partners_guest import PartnerGuest

# Utils
from bk_service.banks.tests.utils.setup import(
    create_partner,
    invite_partner,
    PARTNER_GUEST_NAME_TEST,
    PARTNER_GUEST_PHONE_TEST,
    PHONE_REGION_CODE_TEST
)

# Utils commons
from bk_service.utils.tests.requests import post_with_token
from bk_service.utils.constants_errors import *

# error
from bk_service.utils.constants_errors import build_error_message, PARTNER_GUEST_NOT_EXIST


# import pdb
# pdb.set_trace()

INVITE_PARTNER_GUEST_URL = '/banks/invite-partner-guest/'
DELETE_PARTNER_GUEST_URL = '/banks/delete-partner-guest/'

partners_guest_body = {
    "name": 'manaos',
    "phone_number": '12345678901',
    "phone_region_code": '+1'
}


class InvitePartnerGuestTestCase(APITestCase):
    """invite partner guest test class """

    def setUp(self):
        self.partner = create_partner(phone_number='1234567890')
        self.user = self.partner.user
        invite_partner(bank=self.partner.bank, phone_number='30000000')

    def test_invite_partner_guest_success(self):
        """ invite partner guest success """

        request = post_with_token(
            INVITE_PARTNER_GUEST_URL,
            user=self.user,
            body=partners_guest_body,
        )

        body = request.data

        partner_guest = PartnerGuest.objects.get(phone_number='12345678901')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'partner guest was created')
        self.assertEqual(partner_guest.name, 'manaos')
        self.assertEqual(partner_guest.phone_number, '12345678901')
        self.assertEqual(partner_guest.phone_region_code, '+1')
        self.assertEqual(partner_guest.bank, self.partner.bank)

    def test_invite_partner_guest_phone_exist(self):
        """ delete partner guest fail, phone exist """

        bad_partners_guest_body = partners_guest_body.copy()

        # partner guest phone exist
        bad_partners_guest_body['phone_number'] = '30000000'
        request = post_with_token(
            INVITE_PARTNER_GUEST_URL,
            user=self.user,
            body=bad_partners_guest_body,
        )

        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
            [ErrorDetail(string=build_error_message(PARTNER_GUEST_PHONE_EXIST), code='unique')],
        })

        # partner phone exist

        bad_partners_guest_body['phone_number'] = '1234567890'
        request = post_with_token(
            INVITE_PARTNER_GUEST_URL,
            user=self.user,
            body=bad_partners_guest_body,
        )

        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
            [ErrorDetail(string=build_error_message(PHONE_EXIST), code='unique')],
        })

    def test_invite_partner_guest_body_required(self):
        """ delete partner guest fail, phone exist """

        bad_partners_guest_body = {}

        # partner guest phone exist
        request = post_with_token(
            INVITE_PARTNER_GUEST_URL,
            user=self.user,
            body=bad_partners_guest_body,
        )

        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
                [ErrorDetail(string=build_error_message(PARTNER_GUEST_PHONE_REQUIRED), code='required')],
            'phone_region_code':
                [ErrorDetail(string=build_error_message(PARTNER_GUEST_PHONE_REGION_CODE_REQUIRED), code='required')],
            'name':
                [ErrorDetail(string=build_error_message(PARTNER_GUEST_NAME_REQUIRED), code='required')],
        })


class DeletePartnerGuestTestCase(APITestCase):
    """delete partner guest test class """

    def setUp(self):
        partner = create_partner()
        self.user = partner.user
        invite_partner(bank=partner.bank, phone_number='30000000')

    def test_delete_partner_guest(self):
        """ delete partner guest success """

        body = '30000000'
        request = post_with_token(DELETE_PARTNER_GUEST_URL, user=self.user, body=body,)
        body = request.data

        partner_guest = PartnerGuest.objects.filter(phone_number='30000000')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'partner guest was deleted')
        self.assertEqual(len(partner_guest), 0)

    def test_delete_partner_guest(self):
        """ delete partner guest success """

        body = '30000001'
        request = post_with_token(DELETE_PARTNER_GUEST_URL, user=self.user, body=body,)
        body = request.data

        partner_guest = PartnerGuest.objects.filter(phone_number='30000000')

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=PARTNER_GUEST_NOT_EXIST)})
        self.assertEqual(len(partner_guest), 1)
