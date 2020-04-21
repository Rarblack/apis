from django.contrib import admin
from .models import Announcement
from user.models import CustomUser
from django.shortcuts import redirect
from django.utils import timezone


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id']

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
            obj.updated_datetime = timezone.now()
        else:
            obj.created_by = request.user
        super(AnnouncementAdmin, self).save_model(request, obj, form, change)


