from django.db import models
from user.models import Ord_user, Organizer
from django.core.exceptions import ValidationError
from user.models import Organizer
# from django_admin_geomap import GeoItem


# Create your models here.
class Event_Category(models.Model):
    name = models.CharField(max_length=255)




class Event(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    event_type = models.ForeignKey(Event_Category, on_delete=models.CASCADE)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    min_age = models.IntegerField()
    location = models.TextField(max_length=255)
    image = models.ImageField(upload_to='events_image', default='events_image/logo.png')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    count_user = models.IntegerField(default=0)
    max_capacity = models.IntegerField()
    duration = models.PositiveIntegerField(default=0)


class Favorite(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ord_user = models.ForeignKey(Ord_user, on_delete=models.CASCADE, null=True, blank=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        # Check that at least one of ord_user or organizer is provided
        if not self.ord_user and not self.organizer:
            raise ValidationError('At least one of ord_user or organizer must be provided.')



class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    ord_user = models.ForeignKey(Ord_user, on_delete=models.CASCADE, null=True, blank=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.ord_user and not self.organizer:
            raise ValidationError('At least one of ord_user or organizer must be provided.')






class Event_Statistic(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    number_of_registered_users = models.IntegerField(null=True, blank=True)
    number_of_arrivals = models.IntegerField()
    was_spent = models.IntegerField()
    was_recived = models.IntegerField(null=True, blank=True)
    income = models.IntegerField(null=True, blank=True)
    more_than_aver = models.IntegerField(null=True, blank=True)






