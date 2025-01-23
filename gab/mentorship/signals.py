from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .utils import send_login_email

User = get_user_model()

@receiver(post_save, sender=User)
def send_login_email_signal(sender, instance, created, **kwargs):
    # only send email for newly created users
    if created:
        send_login_email(instance.email, instance.role)