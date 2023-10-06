from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, FavoriteViewSet, ReviewsViewSet, CommentViewSet, EventCategoryViewSet

router = DefaultRouter()
router.register(r'events', viewset = EventViewSet, basename='events')
router.register(r'favorities', viewset = FavoriteViewSet, basename='favorities')
router.register(r'reviews', viewset = ReviewsViewSet, basename='reviews')
router.register(r'comments', viewset = CommentViewSet, basename='comments')
router.register(r'event_categories', viewset = EventCategoryViewSet, basename='event_categories')



urlpatterns = [
    path('', include(router.urls)),
]
