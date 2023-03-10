""" Partners Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.partners import Partner
# Utils
from bk_service.banks.tests.utils.setup import create_partner, PHONE_TEST, PHONE_REGION_CODE_TEST

# Utils Enums
from bk_service.utils.enums.banks import PartnerType


class PartnerTestCase(TestCase):
    """ Partner test class """

    def test_partner_success(self):
        """ Partner success """
        partner_created = create_partner()
        partner = Partner.objects.get(id=partner_created.id)
        self.assertEqual(partner.user.first_name, 'Brea')
        self.assertEqual(partner.bank.name, 'new_bank')

        self.assertEqual(partner.phone_number, PHONE_TEST)
        self.assertEqual(partner.phone_region_code, PHONE_REGION_CODE_TEST)

        self.assertEqual(partner.is_creator, False)
        self.assertEqual(partner.is_active, True)
        self.assertEqual(partner.role, PartnerType.partner)
