""" User models """

# Django

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums import Gender


class User(BkServiceModel, AbstractUser):
    """User model """

    email = models.EmailField(
        'email adress',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='phone number must be entered in the format +9999999999. Up to 15 digits allowed'
    )
    phone_number = models.CharField(max_length=18, blank=False, validators=[phone_regex], unique=True)

    gender = models.CharField(max_length=1, blank=False, choices=Gender.choices)

    city = models.OneToOneField('users.City', on_delete=models.PROTECT)

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text=(
            'Set to true when the user have verified its email address'
        )
    )

    def __str__(self):
        """ Return Username """
        return str(self.username)

    def get_short_name(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'gender', ]
