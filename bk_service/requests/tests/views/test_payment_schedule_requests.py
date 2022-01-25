#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Utils Enums
from bk_service.utils.enums import ApprovalStatus

# Models
from bk_service.requests.models import PaymentScheduleRequest

# Utils test
from bk_service.utils.tests.test_security import security_test_post

URL = '/requests/requests/'


class PaymentScheduleRequestsAPITestCase(APITestCase):
    """ Payment Schedule request test class """

    def setUp(self):
        security_test_post(self=self, URL=URL)

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

    def test_payment_schedule_request_success(self):
        """ payment schedule request success """

        body = {
            'type_request': 'installment_payment',
            'amount': self.schedule_installment.total_pay_installment,
            'id_schedule_installment': self.schedule_installment.id
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'installment_payment request success !')

        payment_schedule_request = PaymentScheduleRequest.objects.get(
            partner=self.partner,
            bank=self.partner.bank,
            schedule_installment=self.schedule_installment
        )
        self.assertEqual(
            payment_schedule_request.amount,
            self.schedule_installment.total_pay_installment
        )
        self.assertEqual(
            payment_schedule_request.approval_status,
            ApprovalStatus.pending,
        )

    def test_payment_schedule_request_fail_pending_request(self):
        """ payment schedule request fail pending request  """
        payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=self.schedule_installment
        )

        body = {
            'type_request': 'installment_payment',
            'amount': self.schedule_installment.total_pay_installment,
            'id_schedule_installment': self.schedule_installment.id
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=PENDING_REQUEST)})

    def test_payment_schedule_request_fail_invalid_amount(self):
        """ payment schedule request fail invalid amount  """

        body = {
            'type_request': 'installment_payment',
            'amount': 0,
            'id_schedule_installment': self.schedule_installment.id
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=AMOUNT_INVALID)})

        # Amount required
        body = {
            'type_request': 'installment_payment',
            'id_schedule_installment': self.schedule_installment.id
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=AMOUNT_INVALID)})

    def test_payment_schedule_request_fail_invalid_id_schedule_installment(self):
        """ payment schedule request fail invalid id schedule installment  """

        # id_schedule_installment required
        body = {
            'type_request': 'installment_payment',
            'amount': 100,
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=ID_SCHEDULE_INSTALMENT_REQUIRED)})

        # id_schedule_installment invalid
        body = {
            'type_request': 'installment_payment',
            'amount': 100,
            # Bad_id
            'id_schedule_installment': 12039712093869
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=ID_SCHEDULE_INSTALMENT_NOT_EXIST)})
