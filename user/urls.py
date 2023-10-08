from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'ord_user', viewset = views.Ord_userView, basename='ord_user')
router.register(r'organizer', viewset = views.OrganizerView, basename='ord_user')





urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/',views.VerificationCodeAPIView.as_view(), name='verify_email' ),
    path('send_ps/', views.SendToRecoverPassword.as_view(), name = 'send_ps'),
    path('check_ps/', views.VerificationPasswordCodeAPIView.as_view(), name = 'check_ps'),
    path('new_ps/', views.NewPasswordView.as_view(), name='new_ps' ),
    path('', include(router.urls)),
]