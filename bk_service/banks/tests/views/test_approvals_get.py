#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import get_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *


# Utils
from bk_service.utils.enums.requests import ApprovalStatus, CreditPayType

# test-utils
from bk_service.utils.tests.test_security import security_test_get

URL = '/banks/approvals/'


class GetApprovalsAPITestCase(APITestCase):
    """ GET approvals test class """

    def setUp(self):
        security_test_get(self=self, URL=URL)

        self.partner = create_partner(role=PartnerType.admin)
        self.share_request = create_share_request(
            partner=self.partner, quantity=20, amount=200000
        )
        self.credit_request = create_credit_request(
            partner=self.partner,
            amount=100000,
            installments=3
        )

        self.credit = create_credit(partner=self.partner, credit_request=self.credit_request)
        self.schedule_installment = create_schedule_installment(self.credit)
        self.payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=self.schedule_installment
        )

    def test_get_approvals_success(self):
        """ GET approvals approve requests success """

        request = get_with_token(URL=URL, user=self.partner.user,)
        body = request.data

        # Bank
        cash_balance = body['cash_balance']
        total_shares_quantity = body['total_shares_quantity']
        total_credits_amount = body['total_credits_amount']
        total_payment_request_amount = body['total_payment_request_amount']

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(cash_balance, 0.0)
        self.assertEqual(total_shares_quantity, 0)
        self.assertEqual(total_credits_amount, 0.0)
        self.assertEqual(total_payment_request_amount, 10000.0)

        # Shares
        shares_request = body['shares_request'][0]
        shares_request_amount = shares_request['amount']
        shares_request_quantity = shares_request['quantity']
        share_partner_id = shares_request['partner']['id']

        self.assertEqual(shares_request_amount, 200000)
        self.assertEqual(shares_request_quantity, 20)
        self.assertEqual(share_partner_id, self.partner.id)

        # Payment
        payment_schedule_request = body['payment_schedule_request'][0]
        payment_schedule_request_amount = payment_schedule_request['amount']
        payment_schedule_request_installment = payment_schedule_request['schedule_installment']

        payment_schedule_request_partner_id = payment_schedule_request['partner']['id']

        self.assertEqual(payment_schedule_request_amount, 10000.0)
        self.assertEqual(payment_schedule_request_partner_id, self.partner.id)
        self.assertEqual(payment_schedule_request_installment, self.schedule_installment.id)

        # Credit
        credit_request = body['credit_request'][0]
        credit_request_amount = credit_request['amount']
        credit_request_installments = credit_request['installments']
        credit_request_credit_use = credit_request['credit_use']
        credit_request_credit_use_detail = credit_request['credit_use_detail']
        credit_request_payment_type = credit_request['payment_type']
        credit_partner_id = credit_request['partner']['id']

        self.assertEqual(credit_request_amount, 100000)
        self.assertEqual(credit_request_installments, 3)
        self.assertEqual(credit_request_credit_use, CreditUse.Consumption)
        self.assertEqual(credit_request_credit_use_detail, CreditUseDetail.Education)
        self.assertEqual(credit_request_payment_type, CreditPayType.installments)
        self.assertEqual(credit_partner_id, self.partner.id)

        # Partner Shares
        partner_shares_request = body['partner_requests']['shares_request'][0]
        partner_shares_request_amount = shares_request['amount']
        partner_shares_request_quantity = shares_request['quantity']
        partner_share_partner_id = shares_request['partner']['id']

        self.assertEqual(partner_shares_request_amount, 200000)
        self.assertEqual(partner_shares_request_quantity, 20)
        self.assertEqual(partner_share_partner_id, self.partner.id)

        # Partner Credit
        partner_credit_request = body['partner_requests']['credit_request'][0]
        partner_credit_request_amount = credit_request['amount']
        partner_credit_request_installments = credit_request['installments']
        partner_credit_request_credit_use = credit_request['credit_use']
        partner_credit_request_credit_use_detail = credit_request['credit_use_detail']
        partner_credit_request_payment_type = credit_request['payment_type']
        partner_credit_partner_id = credit_request['partner']['id']

        self.assertEqual(partner_credit_request_amount, 100000)
        self.assertEqual(partner_credit_request_installments, 3)
        self.assertEqual(partner_credit_request_credit_use, CreditUse.Consumption)
        self.assertEqual(partner_credit_request_credit_use_detail, CreditUseDetail.Education)
        self.assertEqual(partner_credit_request_payment_type, CreditPayType.installments)
        self.assertEqual(partner_credit_partner_id, self.partner.id)

        # Partner Payment
        partner_payment_schedule_request = body['partner_requests']['payment_schedule_request'][0]
        partner_payment_schedule_request_amount = payment_schedule_request['amount']
        partner_payment_schedule_request_installment = payment_schedule_request['schedule_installment']

        partner_payment_schedule_request_partner_id = payment_schedule_request['partner']['id']

        self.assertEqual(partner_payment_schedule_request_amount, 10000.0)
        self.assertEqual(partner_payment_schedule_request_partner_id, self.partner.id)
        self.assertEqual(partner_payment_schedule_request_installment, self.schedule_installment.id)
