""" Shares Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.shares import Share
# Utils
from bk_service.banks.tests.utils.setup import createShare


class SharesTestCase(TestCase):
    """ Shares test class """

    def setUp(self):
        createShare()

    def test_State_success(self):
        """ Shares success """
        share = Share.objects.get(id=1)
        self.assertEqual(share.amount, 10000)
        self.assertEqual(share.quantity, 1)
