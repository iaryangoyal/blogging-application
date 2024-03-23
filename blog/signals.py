from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from user_auth.models import User_login

@receiver(post_save, sender=User_login)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Registration Successful'
        message = 'Thank you for registering with us!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)
