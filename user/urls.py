from django.urls import path
from .views import CustomObtainAuthToken, UsersListAPIView, add_csv_users_to_database

urlpatterns = [
    path('auth-token', CustomObtainAuthToken.as_view()),
    path('', UsersListAPIView.as_view()),
]

urlpatterns += [
    path('add-users-to-database', add_csv_users_to_database, name='users_csv_to_database')
    ]
