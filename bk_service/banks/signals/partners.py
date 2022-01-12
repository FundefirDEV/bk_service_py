""" Partner Signals """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from bk_service.banks.models import Partner, PartnerDetail


@receiver(post_save, sender=Partner)
def post_save_create_partner(sender, instance, created, **kwargs):

    if created:
        PartnerDetail.objects.create(partner=instance)
