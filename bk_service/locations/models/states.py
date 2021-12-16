""" State models """

# Django
from django.db import models

# Models
from .countrys import Country


class State(models.Model):
    """ State model """

    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=18, blank=False, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ Return Username """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'country', ]
