from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import NotificationSerializer
from .models import Notification
from user.models import CustomUser


class NotificationsListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Notification.objects.filter(receivers__pk=self.kwargs['pk'])
