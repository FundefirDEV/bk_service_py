""" Credit Request Test. """

#  Django
from django.test import TestCase
from bk_service.requests.models.credit_requests import CreditRequest

# Utils
from bk_service.banks.tests.utils.setup import create_partner
from bk_service.requests.tests.utils.setup import create_credit_request


class CreditRequestTestCase(TestCase):
    """ Credit Request test class """

    def test_credit_request_success(self):
        """ Credit Request success """
        partner = create_partner()
        create_credit_request(partner)
        creditRequest = CreditRequest.objects.get(partner=partner)
        self.assertEqual(creditRequest.amount, 100000)
        self.assertEqual(creditRequest.installments, 1)
        self.assertEqual(creditRequest.credit_use_detail, '')
        self.assertEqual(creditRequest.credit_use, '')
        self.assertEqual(creditRequest.payment_type, '')
        self.assertEqual(creditRequest.approval_status, '')
