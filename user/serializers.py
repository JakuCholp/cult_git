from rest_framework import serializers
from .models import Ord_user, Organizer
from django.contrib.auth.hashers import make_password

class Ord_userSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = Ord_user
        fields = ('id', 'username','password', 'first_name', 'last_name', 'email' ,'phone_number','date_of_birth', 'gender', 'confirm_password')
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data
    

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        user = Ord_user.objects.create(**validated_data)
        hashed_passw = make_password(user.password)
        user.password = hashed_passw
        user.save()

        return user
    







class VerificationCodeSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length=6, min_length=6, required=True)

    



class OrganizerSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = Organizer
        fields = ('id', 'username','password', 'first_name', 'last_name', 'email' ,'phone_number','date_of_birth', 'gender', 'company_name', 'confirm_password')
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data
    

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        user = Organizer.objects.create(**validated_data)
        hashed_passw = make_password(user.password)
        user.password = hashed_passw
        user.save()

        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
