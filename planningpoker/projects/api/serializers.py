from rest_framework import serializers
from users.api.serializers import UserSerializer

from ..models import Project, ProjectMember



class ProjectMemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ["id", "role", "created_at", "updated_at", "user", "project"]


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
            "uuid",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        return Project.objects.create_project(**validated_data, user=user)


class ProjectSerializer(serializers.ModelSerializer):
    members = ProjectMemberListSerializer(
        many=True, source="get_members", read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "uuid",
            "title",
            "description",
            "members",
            "created_at",
            "updated_at",
        ]
