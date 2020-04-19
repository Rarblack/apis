from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import MessageSerializer, MessageCreateSerializer
from .models import Message
from rest_framework import status
from rest_framework.response import Response


class UserMessagesListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Message.objects.filter(receivers__pk=self.kwargs['pk']).order_by('-created_datetime')


class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



