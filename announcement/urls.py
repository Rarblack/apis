from django.urls import path
from .views import BroadcastAnnouncementsListAPIView, UserAnnouncementsListAPIView, AnnouncementCreateAPIView

app_name = 'announcement'
urlpatterns = [
    path('announcements/broadcast', BroadcastAnnouncementsListAPIView.as_view(), name='list-broadcast-announcements'),
    path('users/<int:pk>/announcements', UserAnnouncementsListAPIView.as_view(), name='list-user-announcements'),
    path('announcements/create', AnnouncementCreateAPIView.as_view(), name='create-announcement'),
]
