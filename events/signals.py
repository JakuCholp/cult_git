
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Event





@receiver(pre_save, sender=Event)
def calculate_duration(sender, instance, **kwargs):
    duration = (instance.end_datetime - instance.start_datetime).seconds // 60
    instance.duration = duration