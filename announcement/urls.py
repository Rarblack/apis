from django.urls import path
from .views import UserAnnouncementsListAPIView, AnnouncementCreateAPIView

app_name = 'announcement'
urlpatterns = [
    path('users/<int:pk>/announcements', UserAnnouncementsListAPIView.as_view(), name='list-announcements'),
    path('announcements/create', AnnouncementCreateAPIView.as_view(), name='create-announcement'),
]
