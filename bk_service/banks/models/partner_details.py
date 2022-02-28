""" PartnerDetail models """

# Django
from django.db import models

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums.banks import Scholarship


class PartnerDetail(BkServiceModel, models.Model):
    """ PartnerDetail model """

    partner = models.OneToOneField('banks.Partner', on_delete=models.CASCADE)

    earnings = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    profit_obtained = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)

    active_credit = models.DecimalField(max_digits=100, decimal_places=4, null=False, default=0.0)
    shares = models.PositiveIntegerField(null=False, default=0,)

    document_number = models.CharField(max_length=30, blank=True,)
    profession = models.CharField(max_length=150, blank=True)
    scholarship = models.CharField(max_length=30, null=False, choices=Scholarship.choices, default=Scholarship.noData)
    birth_date = models.DateTimeField(
        null=True,
    )

    REQUIRED_FIELDS = ['earnings', 'active_credit', 'shares', 'partner']
