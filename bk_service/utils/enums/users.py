# Django
from django.db import models


class Gender(models.TextChoices):
    M = "M"
    F = "F"
    O = "O"
