""" Partner Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from bk_service.banks.models import Bank, BankRules

# Utils enums
from bk_service.utils.bank_rules_constants import BankRulesConstants


@receiver(post_save, sender=Bank)
def post_save_create_bank(sender, instance, created, **kwargs):

    if created:

        bank_rules = BankRulesConstants(country_code=instance.city.state.country.code)

        bank_rules = BankRules.objects.create(
            bank=instance,
            ordinary_interest=bank_rules.ORDINARY_INTEREST,
            delay_interest=bank_rules.DELAY_INTEREST,
            maximun_credit_installments=bank_rules.MAXIMUN_CREDIT_INSTALLMENTS,
            maximun_credit_value=bank_rules.MAXIMUN_CREDIT_VALUE,
            share_value=bank_rules.SHARE_VALUE,
            maximum_shares_percentage_per_partner=bank_rules.MAXIMUM_SHARES_PERCENTAGE_PER_PARTNER,
            maximum_active_credits_per_partner=bank_rules.MAXIMUM_ACTIVE_CREDITS_PER_PARTNER,
            expenditure_fund_percentage=bank_rules.EXPENDITURE_FUND_PERCENTAGE,
            reserve_fund_of_bad_debt_percentage=bank_rules.RESERVE_FUND_OF_BAD_DEBT_PERCENTAGE,
            payment_period_of_installment=bank_rules.PAYMENT_PERIOD_OF_INSTALLMENT,
            credit_investment_relationship=bank_rules.CREDIT_INVESTMENT_RELATIONSHIP,
            is_active=True,
        )
