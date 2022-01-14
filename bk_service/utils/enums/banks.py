# Django
from django.db import models


class PartnerType(models.TextChoices):
    admin = "admin"
    partner = "partner"
    guest = "guest"


class Scholarship(models.TextChoices):
    noData = "noData"
    primary = "primary"
    secondary = "secondary"
    highschool = "highschool"
    university = "university"
    master = "master"
    doctorate = "doctorate"


class PaymentStatus(models.TextChoices):
    pending = "pending"
    complete = "complete"
    incomplete = "incomplete"
