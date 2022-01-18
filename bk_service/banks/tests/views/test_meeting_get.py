#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import get_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import security_test_get

URL = '/banks/meetings/'


class GetMeetingAPITestCase(APITestCase):
    """ GET meeting test class """

    def setUp(self):
        security_test_get(self=self, URL=URL)

        self.partner = create_partner(role=PartnerType.admin)
        self.share_request = create_share_request(
            partner=self.partner, quantity=20, amount=200000
        )
        self.share = create_share(
            partner=self.partner,
            share_request=self.share_request
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
        self.payment_schedule = create_payment_schedules(
            credit=self.credit,
            payment_schedule_request=self.payment_schedule_request
        )

    def test_meeting_get_success(self):
        """ GET meeting approve requests success """

        request = get_with_token(URL=URL, user=self.partner.user,)
        body = request.data

        resource = body['resource']
        cash_balance = body['cash_balance']
        expenditure_fund = body['expenditure_fund']
        reserve_fund_of_bad_debt = body['reserve_fund_of_bad_debt']
        earning_by_share = body['earning_by_share']
        total_shares_quantity = body['total_shares_quantity']
        total_shares_amount = body['total_shares_amount']
        total_delay_interest = body['total_delay_interest']
        total_ordinary_interest = body['total_ordinary_interest']
        total_credits_amount = body['total_credits_amount']
        total_credits_quantity = body['total_credits_quantity']
        capital_balance = body['capital_balance']

        bank = Bank.objects.get(pk=self.partner.bank.pk)

        self.assertEqual(resource, 'PREVIEW')
        self.assertEqual(cash_balance, bank.cash_balance)
        self.assertEqual(expenditure_fund, 50)
        self.assertEqual(reserve_fund_of_bad_debt, 50)
        self.assertEqual(total_shares_quantity, self.share.quantity)
        self.assertEqual(total_shares_amount, self.share.amount)
        self.assertEqual(total_delay_interest, 0)
        self.assertEqual(earning_by_share, 45)
        self.assertEqual(
            total_ordinary_interest, self.payment_schedule.interest_paid)
        self.assertEqual(total_credits_amount, self.credit.amount)
        self.assertEqual(total_credits_quantity, 1)
        self.assertEqual(capital_balance, self.payment_schedule.capital_paid)
