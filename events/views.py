from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Favorite,  Comment, Event_Category, Reviews
from .serializers import EventSerializer, FavoriteSerializer, ReviewsSerializer, CommentSerializer, EventCategorySerializer
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.db.models import Q

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer



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
    

