from django.contrib import admin
from .models import Message
from user.models import CustomUser
from django.shortcuts import redirect
from django.utils import timezone


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id']

    def get_exclude(self, request, obj=None):
        excluded = super().get_exclude(request, obj) or []

        if not obj:
            return excluded + ['receivers']
        return excluded

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     kwargs['queryset'] = CustomUser.objects.exclude(pk=request.user.id)
    #     return super(MessageAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if change:
            obj.receivers.set(form.instance.receivers.all())
            obj.updated_by = request.user
            obj.updated_datetime = timezone.now()
        else:
            obj.created_by = request.user
        super(MessageAdmin, self).save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/admin/message/message/%s/change/' % obj.pk)


