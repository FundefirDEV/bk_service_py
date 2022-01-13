""" Bank test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail


# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.utils.tests.requests import get_with_token, post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.utils.tests.test_security import security_test_post

# Models
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.bank_rules import BankRules


# import pdb

URL = '/banks/bank/'


class BankSuccessAPITestCase(APITestCase):
    """ Bank success test class """

    def setUp(self):
        security_test_post(self=self, URL=URL)
        city = create_locations()
        self.user = create_user(city)
        self.city_id = city.id

    def test_bank_success(self):
        """ Bank success """

        request_data = bank_creation_data(city_id=self.city_id)

        request = post_with_token(URL=URL, user=self.user, body=request_data)

        body = request.data
        status_code = request.status_code

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, {"message": "Bank created"})

        bank = Bank.objects.first()
        bank_rules = BankRules.objects.get(bank=bank)

        partners_guest = PartnerGuest.objects.all()
        partner = Partner.objects.get(bank_id=bank.id)

        self.assertEqual(bank.name, BANK_NAME_TEST)
        self.assertEqual(len(partners_guest), 1)
        self.assertEqual(partner.user, self.user)
        # self.assertEqual(bank.get_rules(), bank_rules)
        self.assertEqual(bank_rules.bank, bank)


class BankFailAPITestCase(APITestCase):
    """ Bank fail test class """

    def setUp(self):

        self.bank = create_bank()
        self.user = create_user(self.bank.city)

    def test_fail_bank_name_exist_and_city_does_exist(self):
        """ fail Bank name exist and city does exist """

        request_data = bank_creation_data(
            city_id=99999,
            bank_name=self.bank.name
        )

        request = post_with_token(URL=URL, user=self.user, body=request_data)

        body = request.data
        status_code = request.status_code

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

        # pdb.set_trace()

        self.assertEqual(
            body,
            {
                'name':
                    [ErrorDetail(string=build_error_message(BANK_NAME_EXIST), code='unique')],
                'city':
                    [ErrorDetail(string=build_error_message(CITY_INVALID), code='does_not_exist')]
            })

    def test_fail_partner_guest_exist(self):
        """ fail partner guest exist """

        partner_guest = invite_partner(bank=self.bank)

        request_data = bank_creation_data(
            city_id=self.bank.city.id,
            bank_name='new bank 2',
            partners_guest=[
                {
                    "name": 'manaos',
                    "phone_number": partner_guest.phone_number,
                    "phone_region_code": partner_guest.phone_region_code

                }
            ]
        )

        request = post_with_token(URL=URL, user=self.user, body=request_data)

        body = request.data
        status_code = request.status_code

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            body,
            {
                'partners':
                    [{'phone_number': [ErrorDetail(
                        string=build_error_message(PARTNER_GUEST_PHONE_EXIST), code='unique')]}]
            })
