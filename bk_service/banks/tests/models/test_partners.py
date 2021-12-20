""" Partners Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.partners import Partner
# Utils
from bk_service.banks.tests.utils.setup import createPartner


class PartnerTestCase(TestCase):
    """ Partner test class """

    def setUp(self):
        createPartner()

    def test_State_success(self):
        """ Partner success """
        partner = Partner.objects.get(id=1)
        self.assertEqual(partner.user.first_name, 'Bre')
        self.assertEqual(partner.bank.name, 'new_bank')
        self.assertEqual(partner.is_creator, False)
        self.assertEqual(partner.is_active, True)
        self.assertEqual(partner.role, '')
