from rest_framework import serializers
from ..models import Notification

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            "id",
            "kind",
            "user",
            "sender",
            "message",
            "context",
            "created_at",
            "updated_at",
            "read_at",
        ]


