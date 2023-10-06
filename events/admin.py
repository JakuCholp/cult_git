from django.contrib import admin
from .models import Event, Favorite, Comment, Event_Category, Reviews

# Register your models here.
admin.site.register(Event)
admin.site.register(Favorite)
admin.site.register(Reviews)
admin.site.register(Comment)
admin.site.register(Event_Category)