#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Models
from bk_service.banks.models import Meeting, Bank

# Utils commons
from bk_service.utils.tests.requests import get_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import (
    security_test_get,
    security_test_partner_admin_get
)

URL = '/banks/shares-current-meeting/'


class SharesCurrentMeetingAPITestCase(APITestCase):
    """ Shares Current meeting test class """

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

    def test_shares_current_meeting_success(self):
        """ test shares current meeting success """

        request = get_with_token(URL=URL, user=self.partner.user,)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)

        # Verify body
        last_cash_balance = body['last_cash_balance']
        total_quantity_shares_meeting = body['total_quantity_shares_meeting']
        new_cash_balance = body['new_cash_balance']
        shares_by_partners = body['shares_by_partners']

        self.assertEqual(last_cash_balance, self.partner.bank.cash_balance)
        self.assertEqual(total_quantity_shares_meeting, self.share.quantity)
        self.assertEqual(new_cash_balance, float(self.partner.bank.cash_balance) + float(self.share.amount))

        self.assertEqual(len(shares_by_partners), 1)
        self.assertEqual(shares_by_partners[0]['partner']['user']['username'], self.partner.user.username)
        self.assertEqual(shares_by_partners[0]['quantity'], self.share.quantity)
        self.assertEqual(shares_by_partners[0]['amount'], self.share.amount)
