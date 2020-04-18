from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        depth = 1
        fields = (
            'title', 'message', 'created_by', 'created_datetime'
        )


class AnnouncementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = (
            'receivers', 'title', 'message', 'created_by'
        )
