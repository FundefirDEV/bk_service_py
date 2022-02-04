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
from bk_service.utils.tests.test_security import security_test_get

URL = '/banks/credits-current-meeting/'


class CreditsCurrentMeetingAPITestCase(APITestCase):
    """ Credits Current meeting test class """

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

    def test_credit_current_meeting_success(self):
        """ test credit current meeting success """

        request = get_with_token(URL=URL, user=self.partner.user,)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)

        # Verify body

        partnerts_payments_schedule = body['partnerts_payments_schedule']
        partnerts_credits = body['partnerts_credits']

        self.assertEqual(len(partnerts_credits), 1)
        self.assertEqual(len(partnerts_payments_schedule), 1)

        # Credit
        partner_credit = partnerts_credits[0]

        self.assertEqual(partner_credit['partner']['user']['username'], self.partner.user.username)
        self.assertEqual(partner_credit['amount'], self.credit.amount)
        self.assertEqual(partner_credit['total_interest'], self.credit.total_interest)
        self.assertEqual(partner_credit['payment_type'], self.credit.payment_type)

        # Payment Schedule

        partner_payment_schedule = partnerts_payments_schedule[0]

        self.assertEqual(partner_payment_schedule['partner']['user']['username'], self.partner.user.username)
        self.assertEqual(
            partner_payment_schedule['capital_paid'],
            self.payment_schedule.capital_paid
        )
        self.assertEqual(
            partner_payment_schedule['ordinary_interest_paid'],
            self.payment_schedule.ordinary_interest_paid
        )
        self.assertEqual(
            partner_payment_schedule['payment_type'],
            self.payment_schedule.payment_type
        )
