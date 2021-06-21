from rest_framework import serializers
from users.api.serializers import UserSerializer

from ..models import Project, ProjectInviteCode, ProjectMember

from stories.api.serializers import StorySerializer


class ProjectMemberDetailSerializer(serializers.ModelSerializer):
    project_id = serializers.UUIDField(write_only=True)
    user_id = serializers.UUIDField(write_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = [
            "id",
            "role",
            "created_at",
            "updated_at",
            "user",
            "user_id",
            "project",
            "project_id",
        ]
        extra_kwargs = {"project": {"read_only": True}, "user": {"read_only": True}}


class ProjectMemberListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = [
            "id",
            "role",
            "created_at",
            "updated_at",
            "user",
        ]


class ProjectListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        return Project.objects.create_project(**validated_data, user=user)


class ProjectSerializer(serializers.ModelSerializer):
    stories = StorySerializer(many=True, source="get_stories", read_only=True)
    members = ProjectMemberListSerializer(
        many=True, source="get_members", read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "stories",
            "members",
            "created_at",
            "updated_at",
        ]


class ProjectInviteCodeSerialiser(serializers.ModelSerializer):
    expires_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ProjectInviteCode
        fields = [
            "id",
            "expires_at",
        ]
