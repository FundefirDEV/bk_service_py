""" Bank Rules Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.bank_rules import BankRules
# Utils
from bk_service.banks.tests.utils.setup import create_bank


class BankRulesTestCase(TestCase):
    """ Bank Rules test class """

    def setUp(self):
        self.bank = create_bank()

    def test_bank_rules_success(self):
        """ Bank Rules success """
        bankRules = BankRules.objects.get(bank=self.bank)
        self.assertEqual(bankRules.bank.name, 'new_bank')
        self.assertEqual(bankRules.ordinary_interest, 3.0)
        self.assertEqual(bankRules.delay_interest, 5.0)
        self.assertEqual(bankRules.maximun_credit_installments, 3)
        self.assertEqual(bankRules.maximun_credit_value, 1000000.0)
        self.assertEqual(bankRules.share_value, 10000.0)
        self.assertEqual(bankRules.expenditure_fund_percentage, 5.0)
        self.assertEqual(bankRules.reserve_fund_of_bad_debt, 5.0)
        self.assertEqual(bankRules.is_active, True)
        self.assertEqual(bankRules.maximum_shares_percentage_per_partner, 25.0)
        self.assertEqual(bankRules.maximum_active_credits_per_partner, 1)
        self.assertEqual(bankRules.payment_period_of_installment, 30)
        self.assertEqual(bankRules.credit_investment_relationship, 5.0)
