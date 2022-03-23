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

SHARE_URL = '/banks/my-shares/'
CREDIT_URL = '/banks/my-credit/'
PAYMENT_SCHEDULE_URL = '/banks/my-payment-schedule/'
EARNING_URL = '/banks/my-earning-shares/'

CLOSE_MEETING_URL = '/banks/meetings/close/'


class ShareListViewAPITestCase(APITestCase):
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

        # self.earning_share = create_earning_share(share=self.share)

    def test_share_list_view_success(self):
        """ Share list view success """

        request = get_with_token(URL=SHARE_URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(body), 1)

        self.assertEqual(body[0]['id'], self.share.id)
        self.assertEqual(body[0]['partner']['id'], self.share.partner.id)

    def test_credit_list_view_success(self):
        """ Credit list view success """

        request = get_with_token(URL=CREDIT_URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(body), 1)

        self.assertEqual(body[0]['id'], self.credit.id)
        self.assertEqual(body[0]['partner']['id'], self.credit.partner.id)

    def test_payment_schedule_list_view_success(self):
        """ Payment Schedule list view success """

        request = get_with_token(URL=PAYMENT_SCHEDULE_URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(body), 1)

        self.assertEqual(body[0]['id'], self.payment_schedule.id)
        self.assertEqual(body[0]['partner']['id'], self.payment_schedule.partner.id)

    def test_earning_shares_list_view_success(self):
        """ Earnings Shares list view success """

        request = get_with_token(URL=EARNING_URL, user=self.partner.user)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(body), 1)

        # self.assertEqual(body[0]['id'], self.share.id)
        self.assertEqual(body[0]['share'], self.share.id)
