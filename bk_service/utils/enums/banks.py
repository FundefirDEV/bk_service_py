# Django
from django.db import models


class PartnerType(models.TextChoices):
    admin = "admin"
    partner = "partner"
    guest = "guest"


class Scholarship(models.TextChoices):
    noData = "noData"
    primary = "primary"
    secundary = "secundary"
    highschool = "highschool"
    university = "university"
    master = "master"
    doctorate = "doctorate"
