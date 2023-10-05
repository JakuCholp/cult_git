from django.shortcuts import render
import jwt
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse


from django.contrib.auth.hashers import check_password
from .models import Ord_user, Organizer

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
        if check_password(password, ord_user.password):
            return 
    except Ord_user.DoesNotExist:
        return None




SECRET_KEY = "django-insecure-hwli-cp!(=ordzt2#=*n_%jego_huyhkw_c(@b7-x6616*tzlg"  

def generate_token(user_name, role):
    payload = {
        'user_name': user_name,
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





@permission_classes([AllowAny])
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')  

        user = None
        if role == 'Organizer':
            user = authenticate_Organizer(username=username, password=password)
        elif role == 'Ord_user':
            user = authenticate_Ord_user(username=username, password=password)

        if user:
            token = generate_token(user.id, role)
            return JsonResponse({'token': token}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
