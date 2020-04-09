from django.urls import path
from .views import BroadcastAnnouncementsListAPIView, UserAnnouncementsListAPIView, AnnouncementCreateAPIView

app_name = 'announcement'
urlpatterns = [
    path('broadcast', BroadcastAnnouncementsListAPIView.as_view(), name='list-broadcast-announcements'),
    path('users/<int:pk>', UserAnnouncementsListAPIView.as_view(), name='list-user-announcements'),
    path('create', AnnouncementCreateAPIView.as_view(), name='create-announcement'),
]
