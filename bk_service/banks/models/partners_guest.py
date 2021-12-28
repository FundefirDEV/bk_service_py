""" Partners Guests models """

# Django
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Utils
from bk_service.utils.models import BkServiceModel

# Utils errors
from bk_service.utils.constants_errors import *

# Models
from .banks import Bank


class PartnerGuest(BkServiceModel, models.Model):
    """ PartnerGuest model """

    # Relations
    bank = models.ForeignKey(
        Bank,
        on_delete=models.PROTECT,
        error_messages={
            'does_not_exist': build_error_message(BANK_INVALID),
            'required': build_error_message(BANK_REQUIRED),
        }
    )

    phone_number = models.CharField(
        max_length=18,
        blank=False,
        unique=True,
        validators=[MinLengthValidator(4)],
        error_messages={
            'required': build_error_message(PARTNER_GUEST_NAME_REQUIRED),
            'unique': build_error_message(PARTNER_GUEST_PHONE_EXIST),
            'invalid': build_error_message(PARTNER_GUEST_NAME_INVALID),
        }
    )
    name = models.CharField(
        max_length=150,
        blank=False,
        validators=[MinLengthValidator(2)],
        error_messages={
            'required': build_error_message(PARTNER_GUEST_NAME_REQUIRED),
            'invalid': build_error_message(PARTNER_GUEST_NAME_INVALID),
        },)

    region_code_regex = RegexValidator(
        regex=r'\+?1?\d{0,9}$',
        message=build_error_message(PARTNER_GUEST_PHONE_REGION_CODE_INVALID),
    )
    phone_region_code = models.CharField(
        max_length=4,
        blank=False,
        validators=[region_code_regex, MinLengthValidator(1)],
        unique=False,
        error_messages={
            'required': build_error_message(PARTNER_GUEST_PHONE_REGION_CODE_REQUIRED),
        }
    )

    is_active = models.BooleanField(default=False, blank=False)

    def __str__(self):
        """ Return Partner guest name """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'phone_number', 'phone_region_code', 'bank', ]
