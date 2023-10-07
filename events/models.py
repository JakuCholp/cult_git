from django.db import models
from user.models import Ord_user, Organizer


# Create your models here.
class Event_Category(models.Model):
    name = models.CharField(max_length=255)




class Event(models.Model):
    title = models.CharField(max_length=255)
    event_type = models.ForeignKey(Event_Category, on_delete=models.CASCADE)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.TextField(max_length=255)
    image = models.ImageField(upload_to='events_image', default='events_image/logo.png')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    count_user = models.IntegerField(default=0)
    max_capacity = models.IntegerField()
    duration = models.PositiveIntegerField(default=0)


class Favorite(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ord_user = models.ForeignKey(Ord_user, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)


class Reviews(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    ord_user = models.ForeignKey(Ord_user, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    ord_user = models.ForeignKey(Ord_user, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)






