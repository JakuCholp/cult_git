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


class EventPostSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 255)
    title = serializers.CharField(max_length = 255)
    event_type_id = serializers.IntegerField()
    description = serializers.CharField(max_length = 255)
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    location = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length = 255)
    ticket_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    count_user = serializers.IntegerField()
    max_capacity = serializers.IntegerField()
    duration = serializers.IntegerField()



class CreateFavoriteSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()
    username = serializers.CharField(max_length = 255)


class CreateCommentSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()
    username = serializers.CharField(max_length = 255)
    text = serializers.CharField(max_length = 255)

