from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Favorite,  Comment, Event_Category, Reviews
from .serializers import EventSerializer, FavoriteSerializer, ReviewsSerializer, CommentSerializer, EventCategorySerializer

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