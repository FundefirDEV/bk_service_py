""" User models """

# Django

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums import Gender

# Models
from bk_service.locations.models import City


class User(BkServiceModel, AbstractUser):
    """User model """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        }
    )

    phone_number = models.CharField(max_length=18, validators=[
        MinLengthValidator(4)],  blank=False, unique=True)

    region_code_regex = RegexValidator(
        regex=r'\+?1?\d{0,9}$',
        message='region code must be entered in the format +999.'
    )
    phone_region_code = models.CharField(max_length=4, blank=False,
                                         validators=[region_code_regex, MinLengthValidator(1)], unique=False)

    gender = models.CharField(max_length=1, blank=False, choices=Gender.choices)

    city = models.ForeignKey(City, on_delete=models.PROTECT)

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
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'phone_region_code', 'gender', 'city']
