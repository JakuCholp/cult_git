from rest_framework import serializers
from .models import Ord_user, Organizer

class Ord_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ord_user
        fields = '__all__'

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'
