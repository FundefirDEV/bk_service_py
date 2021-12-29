""" Bank Rules Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.bank_rules import BankRules
# Utils
from bk_service.banks.tests.utils.setup import create_bank_rules


class BankRulesTestCase(TestCase):
    """ Bank Rules test class """

    def setUp(self):
        create_bank_rules()

    def test_bank_rules_success(self):
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
        self.assertEqual(bankRules.maximum_shares_percentage_per_partner, 0)
        self.assertEqual(bankRules.maximum_active_credits_per_partner, 0)
        self.assertEqual(bankRules.payment_period_of_installment, 0)
        self.assertEqual(bankRules.credit_investment_relationchip, 0)
