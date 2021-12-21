""" Country. """

#  Django
from django.test import TestCase
#  Models
from bk_service.locations.models.countries import Country
# Utils
from bk_service.locations.tests.utils.setup import create_locations


class CountryTestCase(TestCase):
    """ Country test class """

    def setUp(self):
        create_locations('Colombia', 'CO', 'Bogota', 'Bogota')

    def test_Country_success(self):
        """ Country success """
        country = Country.objects.get(name='Colombia')

        self.assertEqual(country.code, 'CO')
        self.assertEqual(country.name, 'Colombia')
        self.assertEqual(country.is_active, True)
