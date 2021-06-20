from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import (
    PlanningSession,
    PlanningSessionComment,
    PlanningSessionParticipant,
    Vote,
)
from .permissions import (
    IsSessionProjectMember,
    SessionCommentAuthorOrReadOnly,
    VoteOwnerOrReadOnly,
)
from .serializers import (
    PlanningSessionSerializer,
    PlanningSessionCommentSerializer,
    VoteSerializer,
)
from projects.models import Project
from projects.api.permissions import IsProjectMemberOrReadOnly


class PlanningSessionGeneric:
    permission_classes = [IsAuthenticated, IsProjectMemberOrReadOnly]
    serializer_class = PlanningSessionSerializer
    queryset = PlanningSession.objects.none()
    lookup_field = "id"

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        queryset = PlanningSession.objects.filter(project__id=project_id)
        return queryset

    def check_project_permissions(self, project_id):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(self.request, project)


class PlanningSessionList(PlanningSessionGeneric, generics.ListCreateAPIView):
    def get(self, request, project_id, *args, **kwargs):
        self.check_project_permissions(project_id)
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, *args, **kwargs):
        self.check_project_permissions(project_id)
        request.data["project_id"] = project_id
        return super().post(request, *args, **kwargs)


class PlanningSessionDetail(
    PlanningSessionGeneric, generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated, IsSessionProjectMember]

    def update_queryset(self, project_id):
        self.queryset = PlanningSession.objects.filter(project__id=project_id)

    def get(self, request, project_id, *args, **kwargs):
        self.update_queryset(project_id)
        return super().get(request, *args, **kwargs)

    def update(self, request, project_id, *args, **kwargs):
        self.update_queryset(project_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, project_id, *args, **kwargs):
        self.update_queryset(project_id)
        return super().destroy(request, *args, **kwargs)


class PlanningSessionCommentGeneric:
    permission_classes = [IsAuthenticated, IsProjectMemberOrReadOnly]
    serializer_class = PlanningSessionCommentSerializer
    queryset = PlanningSessionComment.objects.none()


class PlanningSessionCommentList(
    PlanningSessionCommentGeneric, generics.ListCreateAPIView
):
    def get(self, request, project_id, session_id, *args, **kwargs):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        self.queryset = PlanningSessionComment.objects.filter(
            session__project__id=project_id, session__id=session_id
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, session_id, *args, **kwargs):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        request.data["session_id"] = session_id
        request.data["user_id"] = request.user.id
        return super().post(request, *args, **kwargs)


class PlanningSessionCommentDetail(
    PlanningSessionCommentGeneric, generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated, SessionCommentAuthorOrReadOnly]

    def update_queryset(self, project_id, session_id):
        self.queryset = PlanningSessionComment.objects.filter(
            session__id=session_id, session__project__id=project_id
        )

    def get(self, request, project_id, session_id, *args, **kwargs):
        self.update_queryset(project_id, session_id)
        return super().get(request, *args, **kwargs)

    def update(self, request, project_id, session_id, *args, **kwargs):
        self.update_queryset(project_id, session_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, project_id, session_id, *args, **kwargs):
        self.update_queryset(project_id, session_id)
        return super().destroy(request, *args, **kwargs)


class StoryVoteGeneric:
    permission_classes = [IsAuthenticated, IsProjectMemberOrReadOnly]
    queryset = Vote.objects.none()
    serializer_class = VoteSerializer
    lookup_field = "id"


class StoryVoteList(StoryVoteGeneric, generics.ListCreateAPIView):
    def get(self, request, project_id, story_id, *args, **kwargs):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        self.queryset = Vote.objects.filter(
            story__id=story_id, story__project__id=project_id
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, story_id, *args, **kwargs):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        request.data["story"] = story_id
        request.data["user_id"] = request.user.id
        return super().post(request, *args, **kwargs)


class StoryVoteDetail(StoryVoteGeneric, generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, VoteOwnerOrReadOnly]

    def update_queryset(self, project_id, story_id):
        self.queryset = Vote.objects.filter(
            story__id=story_id, story__project__id=project_id
        )

    def get(self, request, project_id, story_id, *args, **kwargs):
        self.update_queryset(project_id, story_id)
        return super().get(request, *args, **kwargs)

    def update(self, request, project_id, story_id, *args, **kwargs):
        self.update_queryset(project_id, story_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, project_id, story_id, *args, **kwargs):
        self.update_queryset(project_id, story_id)
        return super().destroy(request, *args, **kwargs)
