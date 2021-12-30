""" Verify partner phone !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient


# Utils
from bk_service.utils.loaddata.loaddata import setup_db
from bk_service.banks.tests.utils.setup import create_partner, create_bank, invite_partner

# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.utils.tests.requests import post_with_token

# error
from bk_service.utils.constants_errors import *


# import pdb
# pdb.set_trace()


class VerifyPhonePartnerTestCase(APITestCase):
    """ Verify Phone success test class """

    def setUp(self):
        create_partner(phone_number='30000000')

    def test_verify_partner_phone_success(self):
        """ Verify Partner phone success """

        url = '/banks/verify-partner-phone/31111111/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'phone is valid')

    def test_verify_partner_phone_already_exist(self):
        """ Verify Partner Phone already exist """

        url = '/banks/verify-partner-phone/30000000/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
            [ErrorDetail(string=build_error_message(PHONE_EXIST), code='unique')]
        })

    def test_verify_partner_no_invitation(self):
        """Verify if partner with no invitation exist, response 400"""
        url = '/banks/verify-partner-guest-phone/30000000/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
            [ErrorDetail(string=build_error_message(PHONE_EXIST), code='unique')]
        })


class VerifyPhonePartnerGuestTestCase(APITestCase):
    """ Verify Phone success test class """

    def setUp(self):
        bank = create_bank()
        invite_partner(bank=bank, phone_number='30000000')

    def test_verify_partner_phone_success(self):
        """ Verify Partner Guest phone success """

        url = '/banks/verify-partner-guest-phone/31111111/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'phone is valid')

    def test_verify_partner_phone_already_exist(self):
        """ Verify Partner Guest Phone already exist """

        url = '/banks/verify-partner-guest-phone/30000000/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
            [ErrorDetail(string=build_error_message(PHONE_EXIST), code='unique')]
        })


class VerifyMultiplePhonesTestCase(APITestCase):
    """ Verify Multiple Phones success test class """

    def setUp(self):
        self.partner = create_partner(phone_number='30000000')
        self.invite = invite_partner(bank=self.partner.bank, phone_number='40000000')

    def test_verify_multiple_phone_success(self):
        """ Verify Partner Guest phone success """

        url = '/banks/verify-multiple-phones/'

        phones = ['30000', '40000', '50000']
        request = post_with_token(URL=url, user=self.partner.user, body=phones)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'phone numbers are valid')

    def test_verify_multiple_phone_fail(self):
        """ Verify Partner Guest phone fail """
        url = '/banks/verify-multiple-phones/'

        phones = ['300000', '400000', '500000', '30000000']
        request = post_with_token(URL=url, user=self.partner.user, body=phones)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body,
                         [{}, {}, {}, {'phone_number': [ErrorDetail(
                             string=build_error_message(PHONE_EXIST), code='unique')]}]
                         )
