""" User Test. """

#  Django
from django.test import TestCase
from bk_service.users.models.users import User
from bk_service.locations.tests.utils.setup import create_locations


class UsersTestCase(TestCase):
    """ User test class """

    def setUp(self):
        city = create_locations()
        User.objects.create(username='user@mail.com', email='user@mail.com',
                            first_name='Bre', phone_number='31300000000', city=city, last_name='Bre')

    def test_State_success(self):
        """ User success """
        user = User.objects.get(email='user@mail.com')
        self.assertEqual(user.username, 'user@mail.com')
        self.assertEqual(user.phone_number, '31300000000')
        self.assertEqual(user.last_name, 'Bre')
        self.assertEqual(user.first_name, 'Bre')
