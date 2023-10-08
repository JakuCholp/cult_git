from django.shortcuts import render
import jwt
from datetime import datetime, timedelta
from .serializers import Ord_userSerializer, OrganizerSerializer, LoginSerializer,RecoverPasswordSerializer, VerificationPasswordCodeSerializer, NewPasswordSerializer
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Ord_user, Organizer
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.response import Response
from .serializers import VerificationCodeSerializer
from drf_spectacular.utils import extend_schema
from django.utils import timezone
from django.conf import settings
import random
import smtplib
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password





def authenticate_Organizer(username, password):
    try:
        organizer = Organizer.objects.get(username=username)
        if check_password(password, organizer.password):
            return organizer
    except Organizer.DoesNotExist:
        return None

def authenticate_Ord_user(username, password):
    try:
        ord_user = Ord_user.objects.get(username=username)
        if check_password(password,ord_user.password):
            return ord_user
    except Ord_user.DoesNotExist:
        return None




SECRET_KEY = "django-insecure-hwli-cp!(=ordzt2#=*n_%jego_huyhkw_c(@b7-x6616*tzlg"  

def generate_token(user, role):
    payload = {
        'user_name': user.username,
        'token_type': 'access',
        'role': role,
        'exp': datetime.utcnow() + timedelta(days=1) 
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Токен истек
        return None
    except jwt.InvalidTokenError:
        # Неверный токен
        return None
    



def generate_refresh_token(user, role):
    payload = {
        'user_name': user.username,
        'token_type': 'refresh',
        'role': role,
        'exp': datetime.utcnow() + timedelta(days=30)  
    }
    refresh_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return refresh_token




@permission_classes([AllowAny])
class LoginView(APIView):

    @extend_schema(
        description="user's login",
        request= LoginSerializer,
        responses={200: {"message": "user successfully logged."}}
        )
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')  

        
    
        user = authenticate_Ord_user(username=username, password=password)

        if user:
            access_token = generate_token(user, role)
            token_str = access_token.decode('utf-8')
            refresh_token = generate_refresh_token(user, role)
            ref_token_str = refresh_token.decode('utf-8')
            return JsonResponse({'token': token_str, 'refresh': ref_token_str}, status=200)
        else:
            user = authenticate_Organizer(username=username, password=password)
            if user:
                access_token = generate_token(user, role)
                token_str = access_token.decode('utf-8')
                refresh_token = generate_refresh_token(user, role)
                ref_token_str = refresh_token.decode('utf-8')
                return JsonResponse({'token': token_str, 'refresh': ref_token_str}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)






class Ord_userView(viewsets.ModelViewSet):
    queryset = Ord_user.objects.all()
    serializer_class = Ord_userSerializer


class OrganizerView(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer




class VerificationCodeAPIView(APIView):
    @extend_schema(
        description="verify_email",
        request= VerificationCodeSerializer,
        responses={200: {"message": "mail successfully verified."}}
        )
    
    def post(self, request):
        serializer = VerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            verification_code = serializer.validated_data['verification_code']
            user = Ord_user.objects.filter(email_token=verification_code).first()
            if user:
                my_data = user.date_of_join
                current_time = timezone.now()
                time_difference = current_time - my_data
                time_difference_in_minutes = time_difference.total_seconds() / 60
                if time_difference_in_minutes > 3:
                    user.delete()
                    return Response({'message': "oops"})
                user.is_email_confirmed = True
                user.save()
                return Response({'message': 'Verification code is valid.'}, status=status.HTTP_200_OK)
            else:
                user = Organizer.objects.filter(email_token=verification_code).first()
                if user:
                    my_data = user.date_of_join
                    current_time = timezone.now()
                    time_difference = current_time - my_data
                    time_difference_in_minutes = time_difference.total_seconds() / 60
                    if time_difference_in_minutes > 3:
                        user.delete()
                        return Response({'message': "oops"})
                    user.is_email_confirmed = True
                    user.save()
                    return Response({'message': 'Verification code is valid.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class SendToRecoverPassword(APIView):
    @extend_schema(
        description=" send Recover_token Password",
        request= RecoverPasswordSerializer,
        responses={200: {"message": "code successfully sended."}}
        )
    def post(self, request):
        serializer = RecoverPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']

            verification_code = ''.join([str(random.randint(0, 9)) for i in range(6)])

            try:
                user = Ord_user.objects.get(username=username)
                user.recover_token = verification_code
                user.save()
            except:
                user = Organizer.objects.get(username=username)
                user.recover_token = verification_code
                user.save()
            


        
            subject = 'Восстановление пароля'
            message = f'Здравствуйте, {username}!\n\nВаш код для восстановле пароля: {verification_code}\n\nС уважением,\nВаша команда.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            
            try:

                send_mail(subject, message, from_email, to_email)
                return Response({'message': 'Код отправлен на указанный адрес.'}, status=status.HTTP_200_OK)
            except smtplib.SMTPException:
                return Response({'message': 'Произошла ошибка при отправке письма.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'Неверные данные.'}, status=status.HTTP_400_BAD_REQUEST)




class VerificationPasswordCodeAPIView(APIView):
    @extend_schema(
        description="Recover Password",
        request= VerificationPasswordCodeSerializer,
        responses={200: {"message": "code successfully checked."}}
        )
    
    def post(self, request):
        serializer = VerificationPasswordCodeSerializer(data=request.data)
        if serializer.is_valid():
            verification_code = serializer.validated_data['verification_ps_code']
            user = Ord_user.objects.filter(recover_token=verification_code).first()
            if user:
                return Response({'message': ' code is valid.'}, status=status.HTTP_200_OK)
            else:
                user = Organizer.objects.filter(recover_token=verification_code).first()
                if user:
                    return Response({'message': 'code is valid.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



class NewPasswordView(APIView):
    @extend_schema(
        description="new Password",
        request= NewPasswordSerializer,
        responses={200: {"message": "password successfully changed."}}
        )
    def post(self, request):
        serializer = NewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']
            username = serializer.validated_data['username']
            try:
                user = Ord_user.objects.get(username=username)
            except:
                user = Organizer.objects.get(username=username)

            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                return Response({'message': ' PASSWORD is changed.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'mistake.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


