#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.utils.tests.requests import get_with_token, post_with_token

# Model
from bk_service.banks.models.bank_rules import BankRules

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import security_test_get, security_test_post
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import build_error_message


import pytest


URL = '/banks/bank-rules/'

BODY = {
    'ordinary_interest': 1,
    'delay_interest': 2,
    'maximun_credit_installments': 3,
    'maximun_credit_value': 4,
    'share_value': 5,
    'maximum_shares_percentage_per_partner': 6,
    'maximum_active_credits_per_partner': 7,
    'expenditure_fund_percentage': 8,
    'reserve_fund_of_bad_debt_percentage': 9,
    'payment_period_of_installment': 10,
    'credit_investment_relationship': 11
}


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


class PostBankRulesAPITestCase(APITestCase):
    """ POST BankRules test class """

    def setUp(self):
        security_test_post(self=self, URL=URL)
        self.partner = create_partner()

    def test_bank_rules_success(self):
        """ BankRules Fails user is not admin """
        request = post_with_token(URL=URL, user=self.partner.user, body=BODY)
        self.assertEqual(request.data, {'detail': build_error_message(error=PARTNER_IS_NOT_ADMIN)})

    def test_bank_rules_fail_pending_request(self):
        """ BankRules Fails pending request """
        self.partner.role = PartnerType.admin
        self.partner.save()
        create_share_request(partner=self.partner)
        request = post_with_token(URL=URL, user=self.partner.user, body=BODY)
        self.assertEqual(request.data, {'detail': build_error_message(error=CHANGE_RULES_PENDING_REQUEST)})

    def test_bank_rules_success(self):
        """ BankRules success """
        self.partner.role = PartnerType.admin
        self.partner.save()

        request = post_with_token(URL=URL, user=self.partner.user, body=BODY)

        new_rules = BankRules.objects.get(is_active=True)
        inactive_rules = BankRules.objects.get(is_active=False)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(new_rules.ordinary_interest, BODY['ordinary_interest'])
        self.assertEqual(new_rules.delay_interest, BODY['delay_interest'])
        self.assertEqual(new_rules.maximun_credit_installments, BODY['maximun_credit_installments'])
        self.assertEqual(new_rules.maximun_credit_value, BODY['maximun_credit_value'])
        self.assertEqual(new_rules.share_value, BODY['share_value'])
        self.assertEqual(new_rules.maximum_shares_percentage_per_partner, BODY['maximum_shares_percentage_per_partner'])
        self.assertEqual(new_rules.maximum_active_credits_per_partner, BODY['maximum_active_credits_per_partner'])
        self.assertEqual(new_rules.expenditure_fund_percentage, BODY['expenditure_fund_percentage'])
        self.assertEqual(new_rules.reserve_fund_of_bad_debt_percentage, BODY['reserve_fund_of_bad_debt_percentage'])
        self.assertEqual(new_rules.payment_period_of_installment, BODY['payment_period_of_installment'])
        self.assertEqual(new_rules.credit_investment_relationship, BODY['credit_investment_relationship'])

        self.assertEqual(inactive_rules.ordinary_interest, 3.0000)
