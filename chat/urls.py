from django.urls import path
from .views import UserMessagesListAPIView, MessageCreateAPIView

app_name = 'message'
urlpatterns = [
    path('users/<int:pk>/messages', UserMessagesListAPIView.as_view(), name='list-messages'),
    path('messages/create', MessageCreateAPIView.as_view(), name='create-message'),
]
