""" PaymentScheduleRequest Request Test. """

#  Django
from django.test import TestCase
from bk_service.requests.models.payment_schedule_request import PaymentScheduleRequest

# Utils
from bk_service.banks.tests.utils.setup import create_schedule_installment
from bk_service.requests.tests.utils.setup import create_payment_schedule_request
from bk_service.utils.enums.requests import ApprovalStatus


class PaymentScheduleRequestTestCase(TestCase):
    """ PaymentScheduleRequest Request test class """

    def test_payment_schedule_request_success(self):
        """ PaymentScheduleRequest Request success """
        schedule_installment = create_schedule_installment()
        payment_schedule_request_created = create_payment_schedule_request(
            schedule_installment.credit, schedule_installment)

        payment_schedule_request = PaymentScheduleRequest.objects.get(id=payment_schedule_request_created.id)
        self.assertEqual(payment_schedule_request.amount, 10000)
        self.assertEqual(payment_schedule_request.approval_status, ApprovalStatus.pending)
        self.assertEqual(payment_schedule_request.schedule_installment, schedule_installment)
        self.assertEqual(payment_schedule_request.partner, payment_schedule_request_created.partner)
        self.assertEqual(payment_schedule_request.bank, payment_schedule_request_created.bank)
