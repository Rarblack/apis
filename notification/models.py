from django.db import models
from django.utils import timezone
from django.conf import settings
from jsonfield import JSONField
from user.models import CustomUser


class Notification(models.Model):

    type = models.IntegerField(choices=[
        (0, 'Broadcast'),
        (1, 'Single')
    ])

    receivers = models.ManyToManyField(CustomUser)

    data = JSONField(null=True)

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updatedNotifications',
        related_query_name='updatedNotification',
        editable=False
    )

    updated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    read_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='readNotifications',
        related_query_name='readNotification',
        editable=False
    )

    read_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='createdNotifications',
        related_query_name='createdNotification',
        editable=False
    )

    created_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return str(self.id)
