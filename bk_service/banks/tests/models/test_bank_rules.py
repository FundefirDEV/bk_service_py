""" Bank Rules Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.bank_rules import BankRules
# Utils
from bk_service.banks.tests.utils.setup import createBankRules


class BankRulesTestCase(TestCase):
    """ Bank Rules test class """

    def setUp(self):
        createBankRules()

    def test_State_success(self):
        """ Bank Rules success """
        bankRules = BankRules.objects.get(id=1)
        self.assertEqual(bankRules.bank.name, 'new_bank')
        self.assertEqual(bankRules.ordinary_interest, 0)
        self.assertEqual(bankRules.delay_interest, 0)
        self.assertEqual(bankRules.maximun_credit_installments, 0)
        self.assertEqual(bankRules.maximun_credit_value, 0)
        self.assertEqual(bankRules.share_value, 0)
        self.assertEqual(bankRules.expenditure_fund_percentage, 0)
        self.assertEqual(bankRules.reserve_fund_of_bad_debt, 0)
        self.assertEqual(bankRules.is_active, True)
