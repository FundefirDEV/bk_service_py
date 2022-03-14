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
from bk_service.banks.models import Bank, PartnerDetail, Share

# Utils
from bk_service.utils.enums.requests import ApprovalStatus

# Utils Enums
from bk_service.utils.enums import PartnerType, CreditPayType

URL = '/banks/approvals/'


class CreditApprovalsAPITestCase(APITestCase):
    """ Credit approvals test class """

    def setUp(self):
        self.partner = create_partner(role=PartnerType.admin)
        self.bank = self.partner.bank
        self.share = create_share(
            partner=self.partner, quantity=30, amount=300000
        )
        self.previous_bank_info = Bank.objects.get(pk=self.partner.bank.id)
        self.credit_request = create_credit_request(partner=self.partner)
        security_test_post(self=self, URL=URL)
        security_test_partner_admin_post(
            self=self,
            URL=URL,
            body={
                'type_request': 'credit',
                'request_id': self.credit_request.id,
                'approval_status': 'approved'
            }
        )

    def test_credit_installments_approvals_approve_requests_success(self):
        """ Credit installment approvals approve requests success """
        request_body = {
            'type_request': 'credit',
            'request_id': self.credit_request.id,
            'approval_status': 'approved'
        }
        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        post_bank_info = Bank.objects.get(pk=self.partner.bank.id)
        body = request.data
        credit = Credit.objects.get(credit_request=self.credit_request)
        schedule_installment = ScheduleInstallment.objects.filter(credit=credit)

        partner_detail = self.partner.partner_detail()
        cash_balance_calculated = float(self.previous_bank_info.cash_balance) - float(credit.amount)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'credit approved success !')
        # credit = credit request validation
        self.assertEqual(credit.amount, self.credit_request.amount)
        self.assertEqual(credit.installments, self.credit_request.installments)
        # credit installments created
        self.assertEqual(len(schedule_installment), credit.installments)
        # partner_detail "active_credit" need to change
        self.assertEqual(partner_detail.active_credit, credit.amount)
        # cash balance need to change
        self.assertEqual(post_bank_info.cash_balance, cash_balance_calculated)

    def test_credit_advance_approvals_approve_requests_success(self):

        previous_bank_info = Bank.objects.get(pk=self.partner.bank.id)
        credit_request = create_credit_request(partner=self.partner, payment_type=CreditPayType.advance)
        """ Credit advance approvals approve requests success """
        request_body = {
            'type_request': 'credit',
            'request_id': credit_request.id,
            'approval_status': 'approved'
        }
        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        post_bank_info = Bank.objects.get(pk=self.partner.bank.id)
        body = request.data
        credit = Credit.objects.get(credit_request=credit_request)
        schedule_installment = ScheduleInstallment.objects.filter(credit=credit)

        partner_detail = self.partner.partner_detail()
        cash_balance_calculated = float(self.previous_bank_info.cash_balance) - \
            float(credit.amount) + float(credit.total_interest)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'credit approved success !')
        # credit = credit request validation
        self.assertEqual(credit.amount, self.credit_request.amount)
        self.assertEqual(credit.installments, self.credit_request.installments)
        # credit installments created
        self.assertEqual(len(schedule_installment), credit.installments)
        self.assertEqual(schedule_installment[0].ordinary_interest_calculated, 0)
        # partner_detail "active_credit" need to change
        self.assertEqual(partner_detail.active_credit, float(credit.amount) - float(credit.total_interest))
        # cash balance need to change
        self.assertEqual(post_bank_info.cash_balance, cash_balance_calculated)

    def test_credit_approvals_reject_requests_success(self):
        """ Credit approvals reject requests success """

        request_body = {
            'type_request': 'credit',
            'request_id': self.credit_request.id,
            'approval_status': 'rejected'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data
        partner_detail = self.partner.partner_detail()
        post_bank_info = Bank.objects.get(pk=self.partner.bank.id)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'credit rejected success !')
        self.assertEqual(partner_detail.active_credit, 0)
        self.assertEqual(post_bank_info.cash_balance, self.previous_bank_info.cash_balance)
