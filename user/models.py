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
    photo = models.ImageField(upload_to='profile', default='profile/avatarka.jpg', null = True, blank=True)    
    phone_number = PhoneNumberField(unique = True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth =models.DateField(null=True, blank=True)
    date_of_join = models.DateTimeField(auto_now_add=True)
    email_token = models.IntegerField(null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    recover_token = models.IntegerField(null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=255)
    events = models.ManyToManyField('events.Event', through='OrdUserEvent')
    interests = models.ManyToManyField('events.Event_Category', through='OrdUserInterests')
    is_busy = models.BooleanField(default=False)

    


class OrdUserEvent(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    ord_user = models.ForeignKey(Ord_user, on_delete=models.CASCADE)



class OrdUserInterests(models.Model):
    ord_user = models.ForeignKey('user.Ord_user', on_delete=models.CASCADE)
    interest = models.ForeignKey('events.Event_Category', on_delete=models.CASCADE)


class OrdUserTickets(models.Model):
    ord_user = models.ForeignKey('user.Ord_user', on_delete=models.CASCADE)
    tickets = models.ImageField(default='tickets/QR-cod1.png')





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
    photo = models.ImageField(upload_to='profile', default='profile/avatarka.jpg')    
    phone_number = PhoneNumberField(unique = True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth =models.DateField(null=True, blank=True)
    date_of_join = models.DateTimeField(auto_now_add=True)
    email_token = models.IntegerField(null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    recover_token = models.IntegerField(null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=255)
    events = models.ManyToManyField('events.Event', through='OrganizerUserEvent')
    is_busy = models.BooleanField(default=False)
    interests = models.ManyToManyField('events.Event_Category', through='OrganizerInterests')

    


class OrganizerUserEvent(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    organizer_user = models.ForeignKey('user.Organizer', on_delete=models.CASCADE)


class OrganizerInterests(models.Model):
    organizer = models.ForeignKey('user.Organizer', on_delete=models.CASCADE)
    interest = models.ForeignKey('events.Event_Category', on_delete=models.CASCADE)




