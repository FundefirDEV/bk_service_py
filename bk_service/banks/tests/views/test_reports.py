#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils commons
from bk_service.utils.tests.requests import get_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import security_test_post

# Models
from bk_service.banks.models import Share


# Utils Enums
from bk_service.utils.enums.banks import PartnerType

URL = '/banks/reports/'
CLOSE_MEETING_URL = '/banks/meetings/close/'


class ReportsAPITestCase(APITestCase):
    """ Share approvals test class """

    def setUp(self):
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

        close_meeting = get_with_token(URL=CLOSE_MEETING_URL, user=self.partner.user,)

    def test_reports_view_success(self):
        """ Reports view success """

        request = get_with_token(URL=URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)

        # import pdb
        # pdb.set_trace()

        expenditure_fund = body['expenditure_fund']
        reserve_fund_of_bad_debt = body['reserve_fund_of_bad_debt']
        total_shares_quantity = body['total_shares_quantity']
        total_shares_amount = body['total_shares_amount']
        total_earning = body['total_earning']

        self.assertEqual(expenditure_fund, 50)
        self.assertEqual(reserve_fund_of_bad_debt, 50)
        self.assertEqual(total_shares_quantity, self.share.quantity)
        self.assertEqual(total_shares_amount, self.share.amount)
        self.assertEqual(total_earning, 8900.0)

        shares = body['shares']
        credits = body['credits']
        meetings = body['meetings']

        self.assertEqual(len(shares['shares_per_partner']), 1)
        self.assertEqual(len(credits['credits_per_partner']), 1)

        self.assertEqual(len(meetings), 1)
