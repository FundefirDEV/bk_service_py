""" E2E one meeting test !"""

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
from bk_service.banks.models import *

CREATE_BANK_URL = '/banks/bank/'


class E2EOneMeetingAPITestCase(APITestCase):
    """ Bank success test class """

    def setUp(self):
        security_test_post(self=self, URL=CREATE_BANK_URL)
        city = create_locations()
        self.user = create_user(city)
        self.city_id = city.id
        self.guests = [
            {
                "name": "Gibs",
                "phone_number": "3138129220",
                "phone_region_code": PHONE_REGION_CODE_TEST
            },
            {
                "name": "Alex",
                "phone_number": "3138129221",
                "phone_region_code": PHONE_REGION_CODE_TEST
            },
            {
                "name": "Jaime",
                "phone_number": "3138129222",
                "phone_region_code": PHONE_REGION_CODE_TEST
            }
        ]

    def test_create_bank_success(self):
        """ Bank success and basic rules creation"""

        request_data = bank_creation_data(city_id=self.city_id, partners_guest=self.guests)

        request = post_with_token(URL=CREATE_BANK_URL, user=self.user, body=request_data)

        body = request.data
        status_code = request.status_code

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, {"message": "Bank created"})

        bank = Bank.objects.first()
        bank_rules = bank.get_bank_rules()
        rules_verification = BankRules.objects.get(bank=bank)

        partners_guest = PartnerGuest.objects.all()
        partner = Partner.objects.get(bank_id=bank.id)

        self.assertEqual(bank.name, BANK_NAME_TEST)
        self.assertEqual(len(partners_guest), 3)
        self.assertEqual(partner.user, self.user)
        self.assertEqual(rules_verification, bank_rules)
        self.assertEqual(bank_rules.bank, bank)

        """ singup success with guests partners """

        url_singup = '/users/singup/'
        counter = 1

        for guest in self.guests:
            counter += 1
            singup_data = {
                "password": PASSWORD_TEST,
                "password_confirmation": PASSWORD_TEST,
                "first_name": guest["name"],
                "last_name": "Manaos",
                "gender": "M",
                "city": self.city_id,
                "phone_number": guest["phone_number"],
                "phone_region_code": "+1",
                "email": guest["name"]+"@mail.com",
                "username": guest["name"]+"@mail.com"
            }

            request = self.client.post(url_singup, singup_data, format='json')
            body = request.data
            status_code = request.status_code

            access_token = body['access_token']
            refresh_token = body['refresh_token']
            partner_id = body['partner_id']
            user_id = body['id']

            partner_from_partner_guest = Partner.objects.get(phone_number=guest["phone_number"])

            self.assertEqual(request.status_code, status.HTTP_200_OK)

            self.assertEqual(partner_from_partner_guest.bank, bank)
            self.assertEqual(partner_from_partner_guest.is_active, True)
            self.assertEqual(partner_from_partner_guest.phone_region_code, guest["phone_region_code"])
            self.assertEqual(partner_from_partner_guest.role, PartnerType.partner)

            self.assertIsNotNone(access_token)
            self.assertIsNotNone(refresh_token)
            self.assertIsNotNone(partner_id)
            self.assertIsNotNone(user_id)
