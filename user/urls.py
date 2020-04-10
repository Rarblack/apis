from django.urls import path
from .views import CustomObtainAuthToken, UsersListAPIView

urlpatterns = [
    path('users/token-auth', CustomObtainAuthToken.as_view()),
    path('users', UsersListAPIView.as_view()),
]
