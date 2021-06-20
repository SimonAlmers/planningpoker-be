from rest_framework import serializers
from users.api.serializers import UserSerializer
from stories.api.serializers import StorySerializer
from ..models import (
    PlanningSession,
    PlanningSessionComment,
    PlanningSessionParticipant,
    Vote,
)


class PlanningSessionParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PlanningSessionParticipant
        fields = "__all__"


class PlanningSessionCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(write_only=True)
    session_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = PlanningSessionComment
        fields = [
            "id",
            "user",
            "user_id",
            "text",
            "parent",
            "session",
            "session_id",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "user": {"read_only": True},
            "session": {"read_only": True},
        }


class PlanningSessionSerializer(serializers.ModelSerializer):
    comments = PlanningSessionCommentSerializer(
        many=True, source="planningsessioncomment_set", read_only=True
    )
    participants = PlanningSessionParticipantSerializer(
        many=True, source="planningsessionparticipant_set", read_only=True
    )
    focused_story = StorySerializer(many=False, read_only=True)
    stories = StorySerializer(many=True, read_only=True)
    project_id = serializers.UUIDField(write_only=True)
    focused_story_id = serializers.UUIDField(write_only=True, required=False)

    class Meta:
        model = PlanningSession
        fields = [
            "id",
            "participants",
            "comments",
            "created_at",
            "updated_at",
            "focused_story",
            "focused_story_id",
            "stories",
            "project_id",
        ]
        extra_kwargs = {
            "project": {"read_only": True},
            "focused_story": {"read_only": True},
        }


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Vote
        fields = [
            "id",
            "user",
            "user_id",
            "story",
            "point",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "user": {"read_only": True},
        }
