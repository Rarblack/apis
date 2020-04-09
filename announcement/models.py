from django.db import models
from django.conf import settings
from user.models import CustomUser


class Announcement(models.Model):

    type = models.IntegerField(choices=[
        (0, 'Broadcast'),
        (1, 'Single')
    ])

    receivers = models.ManyToManyField(CustomUser)

    title = models.CharField(max_length=150)
    
    message = models.TextField()
    
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updatedAnnouncements',
        related_query_name='updatedAnnouncement',
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
        blank=True,
        related_name='createdAnnouncements',
        related_query_name='createdAnnouncement',
        editable=False
    )

    created_datetime = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return '%s' % self.title
