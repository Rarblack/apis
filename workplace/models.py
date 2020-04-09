from django.db import models
from django.conf import settings


class Workplace(models.Model):

    name = models.CharField(
        max_length=150
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        null=True,
        blank=True,
        related_name='updatedWorkplaces',
        related_query_name='updatedWorkplace'
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='createdWorkplaces',
        related_query_name='createdWorkplace'
    )

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

