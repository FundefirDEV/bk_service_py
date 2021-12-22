""" Partners Guests models """

# Django
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Utils
from bk_service.utils.models import BkServiceModel

# Models
from .banks import Bank


class PartnerGuest(BkServiceModel, models.Model):
    """ PartnerGuest model """

    # Relations
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)

    phone_number = models.CharField(max_length=18, blank=False,
                                    unique=True, validators=[MinLengthValidator(4)])
    name = models.CharField(max_length=150, blank=False,)

    region_code_regex = RegexValidator(
        regex=r'\+?1?\d{0,9}$',
        message='region code must be entered in the format +999.'
    )
    phone_region_code = models.CharField(max_length=4, blank=False,
                                         validators=[region_code_regex, MinLengthValidator(1)], unique=False)

    is_active = models.BooleanField(default=False, blank=False)

    def __str__(self):
        """ Return Partner guest name """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'phone_number', 'phone_region_code', 'bank', ]
