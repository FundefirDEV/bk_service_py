""" Partners models """

# Django
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.constants_errors import *

# Models
from .partner_details import PartnerDetail
from .banks import Bank


class Partner(BkServiceModel, models.Model):
    """ Partner model """

    # Relations
    bank = models.ForeignKey(
        Bank,
        on_delete=models.PROTECT,
        error_messages={
            'does_not_exist': build_error_message(BANK_INVALID),
            'required': build_error_message(BANK_REQUIRED),
        }
    )
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        error_messages={
            'does_not_exist': build_error_message(USER_INVALID),
            'required': build_error_message(USER_REQUIRED),
        }
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
    role = models.CharField(
        max_length=8,
        null=False,
        choices=PartnerType.choices,
        error_messages={
            'required': build_error_message(PARTNER_ROLE_REQUIRED),
            'invalid': build_error_message(PARTNER_ROLE_INVALID),
        }
    )

    is_active = models.BooleanField(default=True)

    is_creator = models.BooleanField(default=False)

    def __str__(self):
        """ Return Username """
        return str(self.user.username)

    def partner_detail(self):
        """ Return partner detail """

        return PartnerDetail.objects.get(partner_id=self.id)

    REQUIRED_FIELDS = ['phone_number', 'role', 'phone_region_code', 'bank', 'user', ]
