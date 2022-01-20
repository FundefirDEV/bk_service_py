#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Models
from bk_service.banks.models import Bank, PartnerDetail
from bk_service.banks.models.bank_rules import BankRules
from bk_service.requests.models import *

# Utils test
from bk_service.utils.tests.test_security import security_test_post

URL = '/requests/requests/'


class ShareRequestsAPITestCase(APITestCase):
    """ Share request test class """

    def setUp(self):
        security_test_post(self=self, URL=URL)

        self.partner = create_partner()

    def test_share_request_success(self):
        """ Share request success """

        body = {
            'type_request': 'share',
            'quantity': 20
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'share request success !')

        share_request = ShareRequest.objects.get(partner=self.partner, bank=self.partner.bank)
        self.assertEqual(share_request.quantity, 20)

    def test_share_request_success_with_meeting(self):
        """ Share request success with meeting"""
        meeting = create_meeting(bank=self.partner.bank)

        self.partner.bank.shares = 200
        self.partner.bank.cash_balance = 2000000.0
        self.partner.bank.save()

        body = {
            'type_request': 'share',
            'quantity': 20
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'share request success !')
        share_request = ShareRequest.objects.get(partner=self.partner, bank=self.partner.bank)

        self.assertEqual(share_request.quantity, 20)

    def test_share_request_fail_exceed_maximun_quantity(self):
        """ Share request fail exceed maximun quantity  """

        meeting = create_meeting(bank=self.partner.bank)

        body = {
            'type_request': 'share',
            'quantity': 2000
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=MAXIMUN_NUMBER_OF_SHARES)})

    def test_share_request_fail_cero_quantity(self):
        """ Share request fail cero quantity  """

        meeting = create_meeting(bank=self.partner.bank)

        body = {
            'type_request': 'share',
            'quantity': 0
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=QUANTITY_INVALID)})
