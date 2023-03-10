""" Bank Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.banks import Bank
# Utils
from bk_service.banks.tests.utils.setup import create_bank


class BankTestCase(TestCase):
    """ Bank test class """

    def setUp(self):
        create_bank()

    def test_bank_success(self):
        """ Bank success """
        bank = Bank.objects.get(name='new_bank')
        self.assertEqual(bank.name, 'new_bank')
        self.assertEqual(bank.cash_balance, 0)
        self.assertEqual(bank.active_credits, 0)
        self.assertEqual(bank.shares, 0)
        self.assertEqual(bank.expenditure_fund, 0)
        self.assertEqual(bank.reserve_fund_of_bad_debt, 0)
        self.assertEqual(bank.city.name, 'Bogota')
