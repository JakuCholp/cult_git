from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, FavoriteViewSet,  CommentViewSet, EventCategoryViewSet, TodaysEventView, TomorrowEventsView, WeekEventsView, EventStatView,  Event_StatisticView, CreateEventView, CreateFavoriteView, CreateCommentView

router = DefaultRouter()
router.register(r'events', viewset = EventViewSet, basename='events')
router.register(r'favorities', viewset = FavoriteViewSet, basename='favorities')
router.register(r'comments', viewset = CommentViewSet, basename='comments')
router.register(r'event_categories', viewset = EventCategoryViewSet, basename='event_categories')
router.register(r'stat', viewset =  Event_StatisticView, basename='stat')



urlpatterns = [
    path('', include(router.urls)),
    path('today/',TodaysEventView.as_view(), name='today'),
    path('tomorrow/',TomorrowEventsView.as_view(), name='tomorrow'),
    path('week/', WeekEventsView.as_view(), name='week'),
    path('statistic/', EventStatView.as_view(), name = 'static'),
    path('create_event/', CreateEventView.as_view(), name = 'create_event'),
    path('create_favorite/', CreateFavoriteView.as_view(), name = 'create_favorite'),
    path('create_comment/', CreateCommentView.as_view(), name = 'create_comment'),
]
