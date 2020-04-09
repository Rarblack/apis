from django.urls import path
from .views import CustomObtainAuthToken

urlpatterns = [
    path(
        'token-auth/',
        CustomObtainAuthToken.as_view()
    ),
]
