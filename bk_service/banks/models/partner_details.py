""" Partners models """

# Django
from django.db import models

# Utils
from bk_service.utils.models import BkServiceModel
from bk_service.utils.enums.banks import Scholarship


class PartnerDetail(BkServiceModel, models.Model):
    """ PartnerDetail model """

    # partner = models.OneToOneField('banks.Partner', on_delete=models.CASCADE)

    earnings = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    active_credit = models.DecimalField(max_digits=100, decimal_places=4, blank=False, default=0.0)
    shares = models.IntegerField(blank=False, default=0,)

    document_number = models.CharField(max_length=30, blank=True, unique=True)
    profession = models.CharField(max_length=150, blank=True)
    scholarship = models.CharField(max_length=30, blank=False, choices=Scholarship.choices)
    birth_date = models.DateTimeField()

    def __str__(self):
        """ Return Username """
        return str(self.partner.user.username)

    REQUIRED_FIELDS = ['phone_number', 'role', 'bank', 'user', 'partner_detail', ]
