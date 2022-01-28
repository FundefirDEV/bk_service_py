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
from bk_service.utils.enums.banks import PartnerType, PaymentStatus

URL = '/banks/approvals/'


class PaymentScheduleApprovalsAPITestCase(APITestCase):
    """ PaymentSchedule approvals test class """

    def setUp(self):
        self.partner = create_partner(role=PartnerType.admin)
        security_test_post(self=self, URL=URL)
        security_test_partner_admin_post(
            self=self,
            URL=URL,
            body={
                'type_request': 'installment_payment',
                'request_id': 'id',
                'approval_status': 'approved'
            }
        )

        self.share = create_share(partner=self.partner)
        self.credit = create_credit(partner=self.partner)
        self.schedule_installment = create_schedule_installment(self.credit)

        self.pre_cash_balance = Bank.objects.get(pk=self.partner.bank.id).cash_balance

        self.payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=self.schedule_installment, amount=91000
        )

    def test_payment_schedule_approve_requests_success(self):
        """ PaymentSchedule approvals approve requests success """

        request_body = {
            'type_request': 'installment_payment',
            'request_id': self.payment_schedule_request.id,
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'installment_payment approved success !')

        validate_payment_schedule(
            self=self,
            schedule_installment_id=self.schedule_installment.id,
            schedule_installment_payment_status=PaymentStatus.complete,
            payment_schedule_request_id=self.payment_schedule_request.id,
            payment_schedule_request_approval_status=ApprovalStatus.approved,
            amount=self.schedule_installment.total_pay_installment,
            capital_paid=self.schedule_installment.capital_installment,
            interest_paid=self.schedule_installment.interest_calculated,
        )

    def test_payment_schedule_reject_requests_success(self):
        """ PaymentSchedule approvals reject requests success """

        request_body = {
            'type_request': 'installment_payment',
            'request_id': self.payment_schedule_request.id,
            'approval_status': 'rejected'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'installment_payment rejected success !')

        payment_schedule_request = PaymentScheduleRequest.objects.get(pk=self.payment_schedule_request.id)

        self.assertEqual(payment_schedule_request.approval_status, ApprovalStatus.rejected)
        self.assertEqual(payment_schedule_request.partner, self.partner)
        self.assertEqual(payment_schedule_request.bank, self.partner.bank)

        bank = Bank.objects.get(pk=self.partner.bank.id)

        calculate_cash_balance = self.share.amount

        self.assertEqual(bank.cash_balance, calculate_cash_balance)

    def test_payment_schedule_approve_requests_success_payment_capital_incomplete(self):
        """ PaymentSchedule approvals approve requests success capital payment incomplete """

        schedule_installment = create_schedule_installment(self.credit)

        payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=schedule_installment, amount=81000
        )

        request_body = {
            'type_request': 'installment_payment',
            'request_id': payment_schedule_request.id,
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'installment_payment approved success !')

        validate_payment_schedule(
            self=self,
            schedule_installment_id=schedule_installment.id,
            schedule_installment_payment_status=PaymentStatus.pending,
            payment_schedule_request_id=payment_schedule_request.id,
            payment_schedule_request_approval_status=ApprovalStatus.approved,
            amount=81000,
            capital_paid=80000,
            interest_paid=1000
        )

    def test_payment_schedule_approve_requests_success_payment_interest_incomplete(self):
        """ PaymentSchedule approvals approve requests success capital payment incomplete """

        schedule_installment = create_schedule_installment(self.credit)

        payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=schedule_installment, amount=900
        )

        request_body = {
            'type_request': 'installment_payment',
            'request_id': payment_schedule_request.id,
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'installment_payment approved success !')

        validate_payment_schedule(
            self=self,
            schedule_installment_id=schedule_installment.id,
            schedule_installment_payment_status=PaymentStatus.pending,
            payment_schedule_request_id=payment_schedule_request.id,
            payment_schedule_request_approval_status=ApprovalStatus.approved,
            amount=900,
            capital_paid=0,
            interest_paid=900
        )

    def test_payment_schedule_approve_requests_success_payment_credit_advance(self):
        """ PaymentSchedule approvals approve requests success capital payment incomplete """

        credit_request = create_credit_request(
            partner=self.partner,
            payment_type=CreditPayType.advance
        )

        credit = create_credit(partner=self.partner, credit_request=credit_request)
        schedule_installment = create_schedule_installment(
            credit=credit,
            capital_installment=90000,
            ordinary_interest_percentage=1,
            total_pay_installment=90000,
            interest_calculated=0,
        )

        payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=schedule_installment, amount=90000
        )

        request_body = {
            'type_request': 'installment_payment',
            'request_id': payment_schedule_request.id,
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'installment_payment approved success !')

        validate_payment_schedule(
            self=self,
            schedule_installment_id=schedule_installment.id,
            schedule_installment_payment_status=PaymentStatus.complete,
            payment_schedule_request_id=payment_schedule_request.id,
            payment_schedule_request_approval_status=ApprovalStatus.approved,
            amount=90000,
            capital_paid=90000,
            interest_paid=0
        )


def validate_payment_schedule(
    self,
    schedule_installment_id,
    schedule_installment_payment_status,
    payment_schedule_request_id,
    payment_schedule_request_approval_status,
    amount,
    capital_paid,
    interest_paid
):

    schedule_installment = ScheduleInstallment.objects.get(
        pk=schedule_installment_id
    )

    payment_schedule_request = PaymentScheduleRequest.objects.get(
        pk=payment_schedule_request_id
    )

    self.assertEqual(
        schedule_installment.payment_status,
        schedule_installment_payment_status
    )

    self.assertEqual(
        payment_schedule_request.approval_status,
        payment_schedule_request_approval_status
    )

    payment_schedule = PaymentSchedule.objects.get(
        payment_schedule_request=payment_schedule_request
    )

    self.assertEqual(payment_schedule.amount, payment_schedule_request.amount)

    self.assertEqual(payment_schedule.amount, amount)
    self.assertEqual(payment_schedule.capital_paid, capital_paid)
    self.assertEqual(payment_schedule.interest_paid, interest_paid)

    self.assertEqual(payment_schedule.partner, self.partner)
    self.assertEqual(payment_schedule.bank, self.partner.bank)

    bank = Bank.objects.get(pk=self.partner.bank.id)

    calculate_cash_balance = float(self.pre_cash_balance) + float(payment_schedule.amount)

    self.assertEqual(bank.cash_balance, calculate_cash_balance)
