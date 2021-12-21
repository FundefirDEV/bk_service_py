""" City. """

#  Django
from django.test import TestCase
from bk_service.locations.models.cities import City


# Utils
from bk_service.locations.tests.utils.setup import create_locations


class CityTestCase(TestCase):
    """ City test class """

    def setUp(self):
        create_locations('Colombia', 'CO', 'Bogota', 'Bogota')

    def test_State_success(self):
        """ State success """
        city = City.objects.get(name='Bogota')
        self.assertEqual(city.name, 'Bogota')
        self.assertEqual(city.is_active, True)
        self.assertEqual(city.state.name, 'Bogota')
