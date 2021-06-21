from rest_framework import serializers
from users.api.serializers import UserSerializer

from ..models import Story, StoryComment


class StoryReorderSerializer(serializers.Serializer):
    story = serializers.UUIDField()
    index = serializers.IntegerField()

    class Meta:
        fields = [
            "story",
            "index",
        ]


class StoryCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = StoryComment
        fields = [
            "id",
            "text",
            "created_at",
            "updated_at",
            "parent",
            "story",
            "user",
            "user_id",
        ]
        extra_kwargs = {"user": {"read_only": True}}


class StorySerializer(serializers.ModelSerializer):
    comments = StoryCommentSerializer(
        many=True, source="storycomment_set", read_only=True
    )
    project_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Story
        fields = [
            "id",
            "title",
            "description",
            "project",
            "project_id",
            "comments",
            "order",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {"project": {"read_only": True}}
