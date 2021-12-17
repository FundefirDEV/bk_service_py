""" Partners models """

# Django
from django.db import models
from django.core.validators import RegexValidator

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

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='phone number must be entered in the format +9999999999. Up to 15 digits allowed'
    )
    phone_number = models.CharField(max_length=18, blank=False, validators=[phone_regex], unique=True)

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
