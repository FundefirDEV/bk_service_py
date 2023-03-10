""" Shares Request Test. """

#  Django
from django.test import TestCase
from bk_service.requests.models.share_requests import ShareRequest

# Utils
from bk_service.banks.tests.utils.setup import create_partner
from bk_service.requests.tests.utils.setup import create_share_request
from bk_service.utils.enums.requests import ApprovalStatus


class SharesRequestTestCase(TestCase):
    """ Shares Request test class """

    def test_share_request_success(self):
        """ Shares Request success """
        partner = create_partner()
        create_share_request(partner)
        shareRequest = ShareRequest.objects.get(partner=partner)
        self.assertEqual(shareRequest.partner, partner)
        self.assertEqual(shareRequest.bank, partner.bank)

        self.assertEqual(shareRequest.amount, 10000)
        self.assertEqual(shareRequest.quantity, 1)
        self.assertEqual(shareRequest.approval_status, ApprovalStatus.pending)
