""" City models """

# Django
from django.db import models

# Models
from .states import State


class City(models.Model):
    """ City model """

    state = models.ForeignKey(State,  on_delete=models.PROTECT, related_name='cities')
    name = models.CharField(max_length=18, null=False,)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ Return Username """
        return str(self.name)

    REQUIRED_FIELDS = ['name', 'state', ]
