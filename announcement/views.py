from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import AnnouncementSerializer, AnnouncementCreateSerializer
from .models import Announcement
from rest_framework import status
from rest_framework.response import Response


class UserAnnouncementsListAPIView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Announcement.objects.filter(receivers__pk=self.kwargs['pk'])


class AnnouncementCreateAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementCreateSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



