# Django REST Framework
from rest_framework.exceptions import APIException

# from rest_framework.test import APITestCase

# Django
from django.test import TestCase

# Models
from bk_service.banks.models import Bank, BankRules

# Bk core
from bk_service.bk_core_sdk.bk_core_sdk_validations import BkCoreSDKValidations

# Utils setup
from bk_service.banks.tests.utils.setup import *

# Utils error
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *

# Pytest
import pytest


class MaximunNumberOfSharesTest(TestCase):
    """ Test Maximun number of shares validations """

    def setUp(self):
        self.partner = create_partner()
        self.bank_rules = self.partner.bank.get_bank_rules()

    def test_maximun_number_of_shares_cero_quantity(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)

        with pytest.raises(CustomException) as e_info:

            bk_validation.maximun_number_of_shares(
                requested_shares_quantity=0, bank_rules=self.bank_rules
            )

        assert str(e_info.value.detail) == build_error_message(error=QUANTITY_INVALID)

    def test_maximun_number_of_shares_success(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)

        bk_validation.maximun_number_of_shares(requested_shares_quantity=10, bank_rules=self.bank_rules)

    def test_maximun_number_of_shares_fail_with_meeting(self):

        meet = create_meeting(bank=self.partner.bank)
        bk_validation = BkCoreSDKValidations(partner=self.partner)

        with pytest.raises(CustomException) as e_info:
            bk_validation.maximun_number_of_shares(requested_shares_quantity=1000, bank_rules=self.bank_rules)

        assert str(e_info.value.detail) == build_error_message(error=MAXIMUN_NUMBER_OF_SHARES)

    def test_maximun_number_of_shares_success_with_meeting(self):
        meet = create_meeting(bank=self.partner.bank)
        bk_validation = BkCoreSDKValidations(partner=self.partner)

        self.partner.bank.shares = 200
        self.partner.bank.save()

        bk_validation.maximun_number_of_shares(requested_shares_quantity=10, bank_rules=self.bank_rules)
