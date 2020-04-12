from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = Notification
        fields = (
            'id', 'data'
        )
