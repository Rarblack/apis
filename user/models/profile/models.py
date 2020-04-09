from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from department.models import Department
from workplace.models import Workplace


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        related_query_name='profile'
    )

    middle_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    gender = models.IntegerField(
        choices=[
            (0, 'Male'),
            (1, 'Woman')
        ]
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='departments',
        related_query_name='department'
    )

    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        null=True,
        related_name='workplaces',
        related_query_name='workplace'
    )

    employed_datetime = models.DateTimeField(
        null=True,
        blank=True
    )

    birth_date = models.DateField(null=True, blank=True)

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updatedProfiles',
        related_query_name='updatedProfile',
        editable=False
    )

    updated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False

    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='createdProfiles',
        related_query_name='createdProfile',
        editable=False
    )

    created_datetime = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def get_creator(self):
        return self.created_by


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()