from django.contrib import admin
from .models import Ord_user, Organizer, OrganizerInterests, OrdUserEvent, OrganizerUserEvent, OrdUserInterests, OrdUserTickets
# Register your models here.
admin.site.register(Organizer)
admin.site.register(Ord_user)
admin.site.register(OrganizerInterests)
admin.site.register(OrganizerUserEvent)
admin.site.register(OrdUserEvent)
admin.site.register(OrdUserTickets)
admin.site.register(OrdUserInterests)

