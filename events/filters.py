import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    min_ticket_price = django_filters.NumberFilter(field_name='ticket_price', lookup_expr='gte')
    max_ticket_price = django_filters.NumberFilter(field_name='ticket_price', lookup_expr='lte')
    start_datetime_after = django_filters.DateTimeFilter(field_name='start_datetime', lookup_expr='gte')
    start_datetime_before = django_filters.DateTimeFilter(field_name='start_datetime', lookup_expr='lte')
    max_capacity = django_filters.NumberFilter(field_name='max_capacity', lookup_expr='gte')
    min_duration = django_filters.NumberFilter(field_name='duration', lookup_expr='gte')
    class Meta:
        model = Event
        fields = ['event_type', 'min_ticket_price', 'max_ticket_price', 'start_datetime_after', 'start_datetime_before', 'max_capacity', 'min_duration']
        ordering_fields = ['ticket_price', 'start_datetime', 'max_capacity', 'duration', 'count_user']