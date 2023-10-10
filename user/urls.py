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
    path('add_event/<str:username>/<str:role>/<int:event_id>/', views.AddEventView.as_view(), name='add_event'),
    path('user_profile/<str:username>/<str:role>/', views.UserProfileAPIView.as_view(), name='user_profile'),
    path('user_update_profile/<str:username>/<str:role>/', views.UserUpdateAPIVIEW.as_view(), name='user_update_profile'),
    path('comfort_time/', views.Comfort_timeAPI.as_view(), name = 'comfort_time'),
    path('change_photo/', views.Change_photo.as_view(), name = 'change_photo'),

    path('', include(router.urls)),
]