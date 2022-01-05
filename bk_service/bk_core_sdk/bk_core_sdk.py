# Bk core SDK validations
from .bk_core_sdk_validations import BkCoreSDKValidations


class BkCoreSDK():

    def __init__(self, partner):
        self.partner = partner
        self.bank = partner.bank
        self.bk_core_validation = BkCoreSDKValidations(
            partner=self.partner,
        )

    # def shares(self,body_shares):
    #     self.bk_core_validation.maximun_number_of_shares(quantity)
