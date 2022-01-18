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

URL = '/banks/bank-rules/'


class BankRulesAPITestCase(APITestCase):
    """ GET BankRules test class """

    def setUp(self):
        security_test_get(self=self, URL=URL)
        self.partner = create_partner()

    def test_bank_rules_success(self):
        """ BankRules success """

        response = {"bankName": "new_bank",
                    "ordinary_interest": 3.0000,
                    "delay_interest": 5.0000,
                    "maximun_credit_installments": 3,
                    "maximun_credit_value": 1000000,
                    "share_value": 10000,
                    "maximum_shares_percentage_per_partner": 25.0000,
                    "maximum_active_credits_per_partner": 1.0000,
                    "expenditure_fund_percentage": 5.0000,
                    "reserve_fund_of_bad_debt_percentage": 5.0000,
                    "payment_period_of_installment": 30,
                    "credit_investment_relationship": 5.0000}

        request = get_with_token(URL=URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, response)
