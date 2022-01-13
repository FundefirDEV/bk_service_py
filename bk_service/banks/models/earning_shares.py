""" EarningShare models """

# Django
from django.db import models

# Models
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.shares import Share
from bk_service.banks.models.meetings import Meeting

# Utils
from bk_service.utils.models import BkServiceModel


class EarningShare(BkServiceModel, models.Model):

    # Relations
    share = models.ForeignKey(Share, on_delete=models.PROTECT)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    earning_by_share = models.DecimalField(max_digits=100, decimal_places=4)
    total_earning_by_share = models.DecimalField(max_digits=100, decimal_places=4)
    is_paid = models.BooleanField(default=False)

    # (use create at)
    # date_calculated = models.DateTimeField(null=False)

    REQUIRED_FIELDS = [
        'share',
        'meeting',
        'earning_by_share',
        'total_earning_by_share',
        'is_paid',
    ]
