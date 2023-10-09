from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Ord_user, Organizer
import random
import string
from django.core.exceptions import ValidationError



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



@receiver(pre_save, sender=Organizer)
def check_existing_username(sender, instance, **kwargs):
    existing_user = Ord_user.objects.filter(username=instance.username).exists()
    if existing_user:
        raise ValidationError('Пользователь с таким username уже существует в модели OrdUser.')
    


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrganizerUserEvent, OrganizerInterests, OrdUserEvent, OrdUserInterests

@receiver(post_save, sender=OrganizerUserEvent)
def create_organizer_interests(sender, instance, created, **kwargs):
    if created:

        event_category = instance.event.event_type
        organizer_interests = OrganizerInterests.objects.create(
            interest=event_category,
            organizer=instance.organizer_user
        )


@receiver(post_save, sender=OrdUserEvent)
def create_organizer_interests(sender, instance, created, **kwargs):
    if created:

        event_category = instance.event.event_type
        ordUser_interests = OrdUserInterests.objects.create(
            interest=event_category,
            ord_user=instance.ord_user
        )


