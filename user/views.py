from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'user_name': user.profile.get_full_name(),
            'is_staff': user.is_staff
        })


class UsersListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

import csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models.profile.models import Profile
from workplace.models import Workplace
from occupation.models import Occupation
from department.models import Department
from django.http import HttpResponse

@login_required
def add_csv_users_to_database(request):
    if request.user.is_superuser:

        department, created = Department.objects.get_or_create(name='Default', code='D', created_by=request.user)

        with open('employee_numbers_list.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',',)

            for row in reader:
                personal_num = int(row[0].strip('\ufeff'))
                if not CustomUser.objects.filter(personal_number=personal_num):
                    user = CustomUser.objects.create_user(
                        personal_number=personal_num,
                        password='User_%s' % personal_num,
                        first_name=row[1],
                        last_name=row[2],
                    )

                    profile, created = Profile.objects.get_or_create(user=user,  created_by=request.user)

                    occupation, created = Occupation.objects.get_or_create(name=row[3])
                    workplace, created = Workplace.objects.get_or_create(name=row[4])

                    profile.occupation = occupation
                    profile.workplace = workplace
                    profile.department = department
                    profile.save()

        return HttpResponse('Users created')
    return HttpResponse('You are not superuser')





