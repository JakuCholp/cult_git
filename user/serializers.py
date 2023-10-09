from rest_framework import serializers
from .models import Ord_user, Organizer
from django.contrib.auth.hashers import make_password
from .models import OrganizerUserEvent, OrdUserEvent

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



class RecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length = 255)



class VerificationPasswordCodeSerializer(serializers.Serializer):
    verification_ps_code = serializers.CharField(max_length=6, min_length=6, required=True)



class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 255)
    confirm_password = serializers.CharField(max_length = 255)
    username = serializers.CharField(max_length = 255)






class OrganizerUserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizerUserEvent
        fields = '__all__'




class OrdUserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdUserEvent
        fields = '__all__'


# class Compfort_timeSerializer(serializers.Serializer):
#     event_type_id = serializers.IntegerField()
#     max_capacity = serializers.IntegerField()
#     start_datetime = serializers.DateTimeField()
#     min_age = serializers.IntegerField()




class UsersProfileSerializer(serializers.Serializer):
    last_name = serializers.CharField(max_length = 255)
    first_name = serializers.CharField(max_length = 255)
    email = serializers.EmailField()
    role = serializers.CharField(max_length = 255)
    photo = serializers.CharField(max_length = 255)
    phone_number = serializers.CharField(max_length = 255)
    country = serializers.CharField(max_length = 255)




