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

# Models
from bk_service.banks.models.banks import Bank


import pdb

URL = '/banks/bank/'


class BankSuccessAPITestCase(APITestCase):
    """ Bank success test class """

    city_id = 0

    def setUp(self):

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

        partners_guest = PartnerGuest.objects.all()
        partner = Partner.objects.get(bank_id=bank.id)

        self.assertEqual(bank.name, BANK_NAME_TEST)
        self.assertEqual(len(partners_guest), 1)
        self.assertEqual(partner.user, self.user)
