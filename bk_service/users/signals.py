import os
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
# env config
import environ


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    env = environ.Env()
    url_token_plaintext = "?token={}".format(reset_password_token.key)
    code = reset_password_token.key
    user_email = str(reset_password_token.user.email)

    send_mail(
        'Password Reset',
        f'code: {code}',
        env('EMAIL_HOST_USER'),
        [user_email],
        fail_silently=True)
