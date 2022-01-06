from bk_service.utils.exceptions_errors import CustomValidation
from bk_service.utils.constants_errors import *

# Models
from bk_service.banks.models.meetings import Meeting
from bk_service.banks.models.bank_rules import BankRules

# BkCore
from .bk_core import BkCore


class BkCoreSDKValidations():

    def __init__(self, partner):
        self.partner = partner
        self.bank = partner.bank

    # quantity = partners shares + requested shares
    def maximun_number_of_shares(self, quantity):

        if quantity <= 0:
            raise Exception('error')
        # CustomValidation(error=QUANTITY_INVALID)

        count_metting = len(Meeting.objects.filter(bank=self.bank))

        if count_metting > 0:

            bank_rules = BankRules.objects.get(bank=self.bank, is_active=True)
            maximum_shares_percentage = bank_rules.maximum_shares_percentage_per_partner
            total_shares = self.bank.shares

            bk_core = BkCore()

            maximun_number_of_shares = bk_core.maximun_number_of_shares(
                total_shares,
                maximum_shares_percentage,
            )

            if quantity > maximun_number_of_shares:
                raise CustomValidation(error=MAXIMUN_NUMBER_OF_SHARES)
