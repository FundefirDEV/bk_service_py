""" Shares Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.shares import Share
# Utils
from bk_service.banks.tests.utils.setup import create_share


class SharesTestCase(TestCase):
    """ Shares test class """

    def test_share_success(self):
        """ Shares success """
        share_created = create_share()
        share = Share.objects.get(id=share_created.id)
        self.assertEqual(share.amount, 10000)
        self.assertEqual(share.quantity, 1)
        self.assertEqual(share.share_request.partner, share_created.partner)
