""" Partners models """

# Django
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums.banks import PartnerType

# Models
from .partner_details import PartnerDetail
from .banks import Bank


class Partner(BkServiceModel, models.Model):
    """ Partner model """

    # Relations
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=18, blank=False,
                                    unique=True, validators=[MinLengthValidator(4)])

    region_code_regex = RegexValidator(
        regex=r'\+?1?\d{0,9}$',
        message='region code must be entered in the format +999.'
    )
    phone_region_code = models.CharField(max_length=4, blank=False,
                                         validators=[region_code_regex, MinLengthValidator(4)], unique=False)

    role = models.CharField(max_length=8, blank=False, choices=PartnerType.choices)

    temporal_name = models.CharField(max_length=150, blank=True,)

    is_active = models.BooleanField(default=True)

    is_creator = models.BooleanField(default=False)

    def __str__(self):
        """ Return Username """
        return str(self.user.username)

    def partner_detail(self):
        """ Return partner detail """

        return PartnerDetail.objects.get(partner_id=self.id)

    REQUIRED_FIELDS = ['phone_number', 'role', 'bank', 'user', ]
