from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import AnnouncementSerializer
from .models import Announcement
from .shortcuts import send_notification, record_notification


class BroadcastAnnouncementsListAPIView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Announcement.objects.filter(type=0)


class UserAnnouncementsListAPIView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Announcement.objects.filter(type=1, receivers__pk=self.kwargs['pk'])


class AnnouncementCreateAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {
            'title': kwargs['title'],
            'message': kwargs['message'],
            'user': {
                'id': kwargs['user_id'],
                'name': kwargs['name']
            }
        }
        send_notification(data=data, **kwargs)
        record_notification(data=data, created_by=request.user, **kwargs)
        return self.create(request, *args, **kwargs)
