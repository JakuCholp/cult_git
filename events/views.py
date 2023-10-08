from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Event, Favorite,  Comment, Event_Category, Event_Statistic
from .serializers import EventSerializer, FavoriteSerializer, CommentSerializer, EventCategorySerializer, EventStaticSerializer, EventStatSerializer
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from datetime import timedelta
from django_filters import rest_framework as dj_filters
from .filters import EventFilter
from django.db.models import Avg
from decimal import Decimal
from user.models import Ord_user, Organizer
from django.core.exceptions import PermissionDenied
from django.http import Http404
from drf_spectacular.utils import extend_schema

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = EventFilter
    search_fields = ['description', 'location', 'title', 'event_type__name']



class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = Event_Category.objects.all()
    serializer_class = EventCategorySerializer







class TodaysEventView(APIView):
    def get(self,request):
        current_datetime = timezone.now()
        queryset = Event.objects.filter(start_datetime__gte=current_datetime)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TomorrowEventsView(APIView):
    def get(self, request):
        tomorrow_date = timezone.now().date() + timezone.timedelta(days=1)
        queryset = Event.objects.filter(
            Q(start_datetime__gte=tomorrow_date) &
            Q(start_datetime__lt=tomorrow_date + timezone.timedelta(days=1))
        )

        serializer = EventSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    



class WeekEventsView(APIView):
    def get(self, request):

        current_datetime = timezone.now()
        start_of_week = current_datetime - timedelta(days=current_datetime.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = Event.objects.filter(
            Q(start_datetime__gte=start_of_week) &
            Q(start_datetime__lte=end_of_week)
        )

        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class EventStatView(APIView):
    @extend_schema(
        description="method post for statistics",
        request= EventStaticSerializer,
        responses={200: {"message": "statistic is seen."}}
        )
    def post(self, request, *args, **kwargs):
        serializer = EventStaticSerializer(data = request.data)
        if serializer.is_valid():
            event = serializer.validated_data['event']
            number_of_arrivals = serializer.validated_data['number_of_arrivals']
            was_spent = serializer.validated_data['was_spent']
            event = Event.objects.get(id = event)
            event_statistic = Event_Statistic.objects.create(event=event, number_of_arrivals=number_of_arrivals, was_spent=was_spent)

            result_receive = event.ticket_price * event_statistic.number_of_arrivals
            event_statistic.was_recived = result_receive


            income_for_event = result_receive - event_statistic.was_spent
            event_statistic.income = income_for_event
            verage_income = Event_Statistic.objects.aggregate(average_income=Avg('income'))
            average_income_value = verage_income.get('average_income', Decimal('0.00'))
            if average_income_value:
                event_statistic.more_than_aver = income_for_event - average_income_value
            else:
                event_statistic.more_than_aver = 0



            event_statistic.save()
            return Response({'message': 'Event statistics created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class Event_StatisticView(viewsets.ModelViewSet):
    queryset = Event_Statistic.objects.all()
    serializer_class = EventStatSerializer

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method 'POST' not allowed on this endpoint."},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)



