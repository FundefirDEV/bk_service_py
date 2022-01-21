# Django REST Framework
from rest_framework.exceptions import APIException

# from rest_framework.test import APITestCase

# Django
from django.test import TestCase

# Models
from bk_service.banks.models import Bank, BankRules
from bk_service.requests.models import CreditRequest, ShareRequest

# Bk core
from bk_service.bk_core_sdk.bk_core_sdk_validations import BkCoreSDKValidations

# Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.utils.enums.requests import (
    TypeRequest,
    CreditPayType,
    CreditUse,
    CreditUseDetail,
)

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

    """ Test Credit Request validations """

    def test_maximun_number_of_credit_cero_quantity(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)

        with pytest.raises(CustomException) as e_info:

            bk_validation.credit_request_validations(
                requested_amount=0,
                quantity=1,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=AMOUNT_INVALID)

    def test_partner_have_pending_credit_request_quantity(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        CreditRequest.objects.create(partner=self.partner, amount=10000,
                                     bank=self.partner.bank, approval_status=ApprovalStatus.pending)
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=100000,
                quantity=1,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=PENDING_REQUEST)

    def test_credit_request_payment_type_invalid(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=100000,
                quantity=1,
                payment_type=None
            )
        assert str(e_info.value.detail) == build_error_message(error=PAYMENT_TYPE_REQUIRED)

    def test_credit_request_installments_excceded(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=100000,
                quantity=0,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=QUANTITY_INVALID)

    def test_credit_request_installments_excceded(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=100000,
                quantity=69,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=MAX_CREDIT_INSTALLMENTS_EXCCEDED)

    def test_partner_have_pending_credit_request_quantity(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        CreditRequest.objects.create(partner=self.partner, amount=10000,
                                     bank=self.partner.bank, approval_status=ApprovalStatus.pending)
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=100000,
                quantity=1,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=PENDING_REQUEST)

    def test_credit_request_quantity_exceed_cash_balance(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=100000,
                quantity=1,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=CASH_BALANCE_EXCCEDED)

    def test_credit_request_quantity_exceed_max_credit_value(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)
        self.partner.bank.cash_balance = 10000000
        self.partner.bank.save()
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=1000001,
                quantity=1,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=MAX_CREDIT_EXCCEDED)

        def test_credit_request_quantity_exceed_max_credit_value(self):
            bk_validation = BkCoreSDKValidations(partner=self.partner)
        self.partner.bank.cash_balance = 10000000
        self.partner.bank.save()
        with pytest.raises(CustomException) as e_info:
            bk_validation.credit_request_validations(
                requested_amount=10000,
                quantity=1,
                payment_type=CreditPayType.advance
            )
        assert str(e_info.value.detail) == build_error_message(error=MAX_PARTNER_CREDIT_EXCCEDED)

        def test_credit_request_validations_success(self):
            bk_validation = BkCoreSDKValidations(partner=self.partner)
        self.partner.bank.cash_balance = 10000000
        self.partner.bank.save()

        share1 = create_share(partner=self.partner)
        share2 = create_share(partner=self.partner)

        bk_validation.credit_request_validations(
            requested_amount=10000,
            quantity=1,
            payment_type=CreditPayType.advance
        )
