""" Users URLs. """

#  Django
from django.test import TestCase
from bk_service.locations.models.countries import Country


class CountryTestCase(TestCase):
    """ Country test class """

    def setUp(self):
        Country.objects.create(name='ARGENTINA', code='AR')

    def test_Country_success(self):
        """ Country success """
        country = Country.objects.get(name='ARGENTINA')

        self.assertEqual(country.code, 'AR')
        self.assertEqual(country.name, 'ARGENTINA')
        self.assertEqual(country.is_active, True)
