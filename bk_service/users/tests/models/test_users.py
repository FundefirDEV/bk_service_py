""" User Test. """

#  Django
from django.test import TestCase
from bk_service.users.models.users import User
from bk_service.locations.tests.utils.setup import create_locations

# Utils
from bk_service.utils.enums import Gender


class UsersTestCase(TestCase):
    """ User test class """

    def setUp(self):
        self.city = create_locations()
        User.objects.create_user(
            username='user@mail.com',
            email='user@mail.com',
            first_name='Brea',
            phone_number='31300000000',
            city=self.city,
            last_name='Brea',
            gender=Gender.M
        )

    def test_State_success(self):
        """ User success """
        user = User.objects.get(email='user@mail.com')
        self.assertEqual(user.username, 'user@mail.com')
        self.assertEqual(user.phone_number, '31300000000')
        self.assertEqual(user.last_name, 'Brea')
        self.assertEqual(user.city, self.city)
        self.assertEqual(user.gender, Gender.M)
        self.assertEqual(user.is_verified, False)
