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
    path('', include(router.urls)),
]