""" django models utilities """

# Django

from django.db import models

# clase base de la cual todos los modelos van a heredar


class BkServiceModel(models.Model):
    """ Comparte Ride base model"""

    created_at = models.DateTimeField(
        verbose_name='create at',
        auto_now_add=True,
        help_text='Date time on whict the object was created'
    )
    updated_at = models.DateTimeField(
        verbose_name='modified at',
        auto_now=True,
        help_text='Date time on whict the object was last modified'
    )

    class Meta:
        """meta options"""
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']
