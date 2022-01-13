""" User models """

# Django

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums import Gender

# Utils errors
from bk_service.utils.constants_errors import *

# Models
from bk_service.locations.models import City
from bk_service.banks.models import Partner


class User(BkServiceModel, AbstractUser):
    """User model """

    email = models.EmailField(
        'email address',
        unique=True,
        null=False,
        error_messages={
            'required': build_error_message(EMAIL_REQUIRED),
            'unique': build_error_message(EMAIL_EXIST),
            'invalid': build_error_message(EMAIL_INVALID),
        }
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        error_messages={
            'required': build_error_message(USERNAME_REQUIRED),
            'unique': build_error_message(USERNAME_EXIST),
            'invalid': build_error_message(USERNAME_INVALID),
        },
    )

    phone_number = models.CharField(
        max_length=18,
        validators=[
            MinLengthValidator(4)],
        null=False,
        unique=True,
        error_messages={
            'required': build_error_message(PHONE_REQUIRED),
            'unique': build_error_message(PHONE_EXIST),
            'invalid': build_error_message(PHONE_INVALID),
        }
    )

    region_code_regex = RegexValidator(
        regex=r'\+?1?\d{0,9}$',
        message=build_error_message(PHONE_REGION_CODE_INVALID),
    )
    phone_region_code = models.CharField(
        max_length=4,
        null=False,
        validators=[region_code_regex, MinLengthValidator(1)],
        error_messages={
            'required': build_error_message(PHONE_REGION_CODE_REQUIRED),
        }
    )

    gender = models.CharField(
        max_length=1,
        null=False,
        choices=Gender.choices,
        error_messages={
            'required': build_error_message(GENDER_INVALID),
            'invalid': build_error_message(GENDER_REQUIRED),
        }
    )

    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        null=True,
        error_messages={
            # 'required': build_error_message(CITY_INVALID),
            'invalid': build_error_message(CITY_REQUIRED),
            'does_not_exist': build_error_message(CITY_INVALID)
        })

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

    def get_partner(self):
        try:
            partner = Partner.objects.get(user_id=self.id)
            return partner
        except:
            return None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'phone_region_code', 'gender', ]
