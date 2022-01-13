""" ScheduleInstallments Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.schedule_installments import ScheduleInstallment
# Utils
from bk_service.banks.tests.utils.setup import create_credit, create_schedule_installment
from bk_service.utils.enums.banks import PaymentStatus


class ScheduleInstallmentsTestCase(TestCase):
    """ ScheduleInstallments test class """

    def test_schedule_installment_success(self):
        """ ScheduleInstallments success """
        credit = create_credit()
        schedule_installment_created = create_schedule_installment(credit=credit)
        schedule_installment = ScheduleInstallment.objects.get(id=schedule_installment_created.id)
        self.assertEqual(schedule_installment.credit, credit)
        self.assertEqual(schedule_installment.capital_installment, 90000)
        self.assertEqual(schedule_installment.ordinary_interest_percentage, 1)
        self.assertEqual(schedule_installment.interest_calculated, 1000)
        self.assertEqual(schedule_installment.total_pay_installment, 0)
        self.assertEqual(schedule_installment.payment_status, PaymentStatus.pending)
        self.assertEqual(schedule_installment.credit, schedule_installment_created.credit)
