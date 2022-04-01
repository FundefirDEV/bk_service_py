# Python
from datetime import timedelta

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import (
    security_test_post,
    security_test_partner_admin_post
)

# Models
from bk_service.banks.models import Bank, Credit, ScheduleInstallment

# Utils
from bk_service.utils.enums.requests import ApprovalStatus

# Utils Enums
from bk_service.utils.enums import PartnerType, CreditPayType

URL = '/banks/special-credit/'


class SpecialCreditAPITestCase(APITestCase):
    """ Special Credit test class """

    def setUp(self):
        self.partner = create_partner(role=PartnerType.admin)
        self.bank = self.partner.bank
        self.share = create_share(
            partner=self.partner, quantity=30, amount=300000
        )
        self.previous_bank_info = Bank.objects.get(pk=self.partner.bank.id)

    def test_special_credit_success(self):
        """ Special Credit success """
        request_body = {
            'installments': 3,
            'ordinary_interest': 3,
            'delay_interest': 5,
            'payment_period_of_installments': 30,
            'amount': 20000,
            'credit_use': 'generationIncome',
            'credit_use_detail': 'smallcompany',
            'payment_type': 'advance',
            'partner_id': self.partner.id
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        credit_validation = Credit.objects.get(partner=self.partner)
        schedule_installments_validation = ScheduleInstallment.objects.filter(credit=credit_validation)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(credit_validation.installments, 3)
        self.assertEqual(credit_validation.amount, 20000)
        self.assertEqual(credit_validation.credit_use, 'generationIncome')
        self.assertEqual(credit_validation.credit_use_detail, 'smallcompany')
        self.assertEqual(credit_validation.payment_type, 'advance')
        self.assertEqual(len(schedule_installments_validation), 3)
        self.assertEqual(schedule_installments_validation[0].ordinary_interest_percentage, 3)
        self.assertEqual(schedule_installments_validation[0].delay_interest_percentage, 5)

    def test_special_credit_fail_cash_balance(self):
        """ Special Credit fail cash balance """
        request_body = {
            'installments': 3,
            'ordinary_interest': 3,
            'delay_interest': 5,
            'payment_period_of_installments': 30,
            'amount': 200000000000,
            'credit_use': 'generationIncome',
            'credit_use_detail': 'smallcompany',
            'payment_type': 'advance',
            'partner_id': self.partner.id
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.data, {'detail': 'error_message : Request quantity exceed Cash balance , error_code : 70'})

    def test_special_credit_fail_invalid_partner_id(self):
        """ Special Credit fail invalid partner"""
        request_body = {
            'installments': 3,
            'ordinary_interest': 3,
            'delay_interest': 5,
            'payment_period_of_installments': 30,
            'amount': 20000,
            'credit_use': 'generationIncome',
            'credit_use_detail': 'smallcompany',
            'payment_type': 'advance',
            'partner_id': 100000
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        self.assertEqual(request.status_code, 404)