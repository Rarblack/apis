from django.db import models
from django.conf import settings

from workplace.models import Workplace


class Department(models.Model):

    name = models.CharField(max_length=150)

    code = models.CharField(max_length=250)

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   models.CASCADE,
                                   null=True,
                                   blank=True,
                                   related_name='updatedDepartments',
                                   related_query_name='updatedDepartment')

    updated_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='createdDepartments',
                                   related_query_name='createdDepartment')

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code'],
                name='department_code_constraint'
            )
        ]

    def __str__(self):
        return '%s' % self.name

