""" State. """

#  Django
from django.test import TestCase
from bk_service.locations.models.countries import Country
from bk_service.locations.models.states import State

# Utils
from bk_service.locations.test.utils.setup import createLocations


class StateTestCase(TestCase):
    """ State test class """

    def setUp(self):
        createLocations('Colombia', 'CO', 'Bogota', 'Bogota')

    def test_State_success(self):
        """ State success """
        state = State.objects.get(name='Bogota')
        self.assertEqual(state.name, 'Bogota')
        self.assertEqual(state.is_active, True)
        self.assertEqual(state.country.name, 'Colombia')
        self.assertEqual(state.country.code, 'CO')
