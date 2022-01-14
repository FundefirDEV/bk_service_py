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

# test-utils
from bk_service.utils.tests.test_security import security_test_get

# Python
from decimal import Decimal


URL = '/banks/bank-detail/'


class BankDetailAPITestCase(APITestCase):
    """ GET BankDetail test class """

    def setUp(self):
        security_test_get(self=self, URL=URL)
        self.partner = create_partner()
        self.bank = self.partner.bank
        self.bank.shares = 100
        self.bank.save()

    def test_bank_rules_success(self):
        """ BankDetail success """

        response = {"rules": {"share_value": Decimal('10000.0000'),
                              "maximum_shares_percentage_per_partner": 0},
                    "group": {"cash_balance": Decimal('0.0000'),
                              "active_credits": Decimal('0.0000'),
                              "shares": 100},
                    "partner": {"earnings": Decimal('0.0000'),
                                "active_credits": Decimal('0.0000'),
                                "shares": 0},
                    }

        request = get_with_token(URL=URL, user=self.partner.user)
        body = dict(request.data)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, response)

    def test_bank_rules_with_meet_success(self):
        """ BankDetail success """

        meeting = create_meeting(bank=self.bank)

        response = {"rules": {"share_value": Decimal('10000.0000'),
                              "maximum_shares_percentage_per_partner": Decimal('25')},
                    "group": {"cash_balance": Decimal('0.0000'),
                              "active_credits": Decimal('0.0000'),
                              "shares": 100},
                    "partner": {"earnings": Decimal('0.0000'),
                                "active_credits": Decimal('0.0000'),
                                "shares": 0},
                    }

        request = get_with_token(URL=URL, user=self.partner.user)
        body = dict(request.data)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, response)
