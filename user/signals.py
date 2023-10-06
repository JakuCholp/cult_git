from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Ord_user, Organizer
import random
import string



def generate_verification_code(length=6):
    characters = string.digits 
    verification_code = ''.join(random.choice(characters) for i in range(length))
    return verification_code


@receiver(post_save, sender=Ord_user)
def send_verification_code(sender, instance, created, **kwargs):
    if created:
        verification_code = generate_verification_code()
        instance.email_token = verification_code  
        instance.save()
        email = instance.email  

        send_mail(
            'Verification Code',
            f'Your verification code is: {verification_code}',
            settings.EMAIL_HOST_USER, 
            [email], 

        )



@receiver(post_save, sender=Organizer)
def send_verification_code_org(sender, instance, created, **kwargs):
    if created:
        verification_code = generate_verification_code()
        instance.email_token = verification_code 
        instance.save()
        email = instance.email 

        send_mail(
            'Verification Code',
            f'Your verification code is: {verification_code}',
            settings.EMAIL_HOST_USER,
            [email], 

        )
