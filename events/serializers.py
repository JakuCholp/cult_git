from rest_framework import serializers
from .models import Event, Favorite,Comment, Event_Category, Reviews

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'



class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Category
        fields = '__all__'

