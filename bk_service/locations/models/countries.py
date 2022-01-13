""" Country models """

# Django
from django.db import models


class Country(models.Model):
    """ Country model """

    name = models.CharField(max_length=18, null=False, unique=True)
    code = models.CharField(max_length=3, null=False, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ Return Username """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'code', ]
