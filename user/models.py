from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models




class Ord_user(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(unique=True)
    role = 'Ord_user'
    photo = models.ImageField(upload_to='profile', default='profile/logo.png')    
    phone_number = PhoneNumberField(unique = True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth =models.DateField(null=True, blank=True)
    date_of_join = models.DateTimeField(auto_now_add=True)
    email_token = models.IntegerField(null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    recover_token = models.IntegerField(null=True, blank=True)





class Organizer(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    role = 'Organizer'
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='profile', default='profile/logo.png')    
    phone_number = PhoneNumberField(unique = True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth =models.DateField(null=True, blank=True)
    date_of_join = models.DateTimeField(auto_now_add=True)
    email_token = models.IntegerField(null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    recover_token = models.IntegerField(null=True, blank=True)

