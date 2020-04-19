from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        depth = 1
        fields = (
            'title', 'message', 'created_by', 'created_datetime'
        )


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = (
            'receivers', 'title', 'message', 'created_by'
        )
