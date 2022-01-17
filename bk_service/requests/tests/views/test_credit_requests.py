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

# Utils
from bk_service.utils.tests.test_security import security_test_post
from bk_service.utils.enums.requests import CreditPayType, TypeRequest, CreditUse, CreditUseDetail

URL = '/requests/requests/'


class ShareRequestsAPITestCase(APITestCase):
    """ Share request test class """

    def setUp(self):
        security_test_post(self=self, URL=URL)

        self.partner = create_partner()
        create_share(partner=self.partner, quantity=10, amount=100000)
        bank = self.partner.bank
        bank.cash_balance = 100000
        bank.save()

    def test_credit_request_success(self):
        """ Credit request success """

        body = {
            'type_request': TypeRequest.credit,
            'amount': 10000,
            'quantity': 3,
            'credit_use': CreditUse.generationIncome,
            'credit_use_detail': CreditUseDetail.trade,
            'payment_type': CreditPayType.installments
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'credit request success !')

        credit_request = CreditRequest.objects.get(partner=self.partner, bank=self.partner.bank)
        self.assertEqual(credit_request.installments, 3)

    def test_credit_request_fail_exceed_maximun_installments(self):
        """ credit request fail """

        body = {
            'type_request': TypeRequest.credit,
            'amount': 10000,
            'quantity': 10,
            'credit_use': CreditUse.generationIncome,
            'credit_use_detail': CreditUseDetail.trade,
            'payment_type': CreditPayType.installments
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=MAX_CREDIT_INSTALLMENTS_EXCCEDED)})

    def test_credit_request_fail_pending_request(self):
        """ credit request fail """
        create_credit_request(self.partner)

        body = {
            'type_request': TypeRequest.credit,
            'amount': 10000,
            'quantity': 3,
            'credit_use': CreditUse.generationIncome,
            'credit_use_detail': CreditUseDetail.trade,
            'payment_type': CreditPayType.installments
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=PENDING_REQUEST)})
