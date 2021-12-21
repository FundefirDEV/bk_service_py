""" PaymentSchedule Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.payment_schedules import PaymentSchedule
# Utils
from bk_service.banks.tests.utils.setup import create_payment_schedules


class PaymentScheduleTestCase(TestCase):
    """ PaymentSchedule test class """

    def test_payment_schedule_success(self):
        """ payment schedule success """
        payment_schedule_created = create_payment_schedules()
        payment_schedule = PaymentSchedule.objects.get(id=payment_schedule_created.id)
        self.assertEqual(payment_schedule.amount, 10000)
        self.assertEqual(payment_schedule.bank, payment_schedule_created.bank)
        self.assertEqual(payment_schedule.partner, payment_schedule_created.partner)
        self.assertEqual(payment_schedule.payment_schedule_request, payment_schedule_created.payment_schedule_request)
        self.assertEqual(payment_schedule.interest_paid, 0)
        self.assertEqual(payment_schedule.capital_paid, 0)
