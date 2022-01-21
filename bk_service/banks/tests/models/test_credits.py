""" Credits Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.credits import Credit
# Utils
from bk_service.banks.tests.utils.setup import create_credit
from bk_service.utils.enums.requests import CreditPayType


class CreditsTestCase(TestCase):
    """ Credits test class """

    def test_credit_success(self):
        """ Credits success """
        credit_created = create_credit()
        credit = Credit.objects.get(id=credit_created.id)
        self.assertEqual(credit.amount, 100000)
        self.assertEqual(credit.installments, 1)
        self.assertEqual(credit.total_interest, 3000.0000)
        self.assertEqual(credit.credit_request.partner, credit_created.partner)
        self.assertEqual(credit.credit_use, '')
        self.assertEqual(credit.credit_use_detail, '')
        self.assertEqual(credit.payment_type, CreditPayType.installments)
        self.assertEqual(credit.is_active, True)
