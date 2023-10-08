from rest_framework import serializers
from .models import Event, Favorite,Comment, Event_Category, Event_Statistic
from user.models import Organizer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'





class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Category
        fields = '__all__'



class EventStaticSerializer(serializers.Serializer):
    event = serializers.IntegerField()
    number_of_arrivals = serializers.IntegerField()
    was_spent = serializers.IntegerField()




class EventStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Statistic
        fields = '__all__'


