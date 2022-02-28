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

URL = '/banks/profit-payment-partners/'
CLOSE_MEETING_URL = '/banks/meetings/close/'


class ProfitPaymentPartnersAPITestCase(APITestCase):
    """ GET profit payment partners test class """

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

        close_meeting = get_with_token(URL=CLOSE_MEETING_URL, user=self.partner.user,)

    def test_profit_payment_partners_get_success(self):
        """ test GET profit_payment_partners success """

        request = get_with_token(URL=URL, user=self.partner.user,)
        body = request.data

        total_profit_obtained = body['total_profit_obtained']
        partners = body['partners']

        self.assertEqual(request.status_code, status.HTTP_200_OK)

        self.assertEqual(total_profit_obtained, 0.0)
        self.assertEqual(len(partners), 1)
        self.assertEqual(partners[0]['partner']['user']['email'], 'user@mail.com')
