#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.users.tests.utils.commons import *

# Model
from bk_service.banks.models.credits import Credit

# Banks test Utils
from bk_service.banks.tests.utils.setup import *

# Utils
from bk_service.utils.enums.requests import ApprovalStatus

# Pytest
import pytest


class BankDetailAPITestCase(APITestCase):
    """ BankDetail Signal test class """

    def setUp(self):
        self.partner = create_partner()
        self.bank = self.partner.bank
        self.bank.shares = 100
        self.bank.save()
        self.credit_request = create_credit_request(partner=self.partner)

    def test_credits_signal_approve_credit(self):
        self.credit_request.approval_status = ApprovalStatus.approved
        self.credit_request.save()
        credit = Credit.objects.get(partner=self.partner)
        self.assertEqual(credit.credit_request, self.credit_request)

    def test_credits_signal_reject_credit(self):
        self.credit_request.approval_status = ApprovalStatus.rejected
        self.credit_request.save()

        with pytest.raises(Exception) as e_info:
            credit = Credit.objects.get(partner=self.partner)

        self.assertEqual(str(e_info.value), 'Credit matching query does not exist.')
