from projects.api.permissions import IsProjectMemberOrReadOnly, ProjectIsMember
from projects.models import Project
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Story, StoryComment
from .permissions import StoryCommentAuthorOrReadOnly, StoryPermissionIsMemberOrReadOnly
from .serializers import StoryCommentSerializer, StoryReorderSerializer, StorySerializer


class StoryGeneric:
    queryset = Story.objects.none()
    serializer_class = StorySerializer
    search_fields = ["title", "description"]


class StoryList(StoryGeneric, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsProjectMemberOrReadOnly]

    def get(self, request, project_id, *args, **kwargs):
        project = Project.objects.get(pk=project_id)
        self.check_object_permissions(request, project)
        self.queryset = Story.objects.filter(project__pk=project_id)
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, *args, **kwargs):
        project = Project.objects.get(pk=project_id)
        self.check_object_permissions(request, project)
        request.data["project"] = project_id
        request.data["requester"] = request.user.pk
        return super().post(request, *args, **kwargs)


class StoryDetail(StoryGeneric, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, StoryPermissionIsMemberOrReadOnly]

    def update_queryset(self, project_id):
        self.queryset = Story.objects.filter(project=project_id)

    def get(self, request, project_id, *args, **kwargs):
        self.update_queryset(project_id)
        return super().get(request, *args, **kwargs)

    def update(self, request, project_id, *args, **kwargs):
        self.update_queryset(project_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, project_id, *args, **kwargs):
        self.update_queryset(project_id)
        return super().destroy(request, *args, **kwargs)


class StoryReorder(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsProjectMemberOrReadOnly]
    serializer_class = StoryReorderSerializer
    queryset = Story.objects.none()
    lookup_field = "project_id"

    def update(self, request, project_id, *args, **kwargs):
        project = Project.objects.get(pk=project_id)
        self.check_object_permissions(request, project)
        # TODO June 13, 2021: Implement Reporder functions
        return super().update(request, *args, **kwargs)


class StoryCommentGeneric:
    permission_classes = [IsAuthenticated, StoryPermissionIsMemberOrReadOnly]
    serializer_class = StoryCommentSerializer
    queryset = StoryComment.objects.none()


class StoryCommentList(StoryCommentGeneric, generics.ListCreateAPIView):
    def get(self, request, project_id, story_id, *args, **kwargs):
        story = Story.objects.get(pk=story_id)
        self.check_object_permissions(request, story)

        self.queryset = StoryComment.objects.filter(
            story__pk=story_id, story__project__pk=project_id
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, story_id, *args, **kwargs):
        story = Story.objects.get(pk=story_id)
        self.check_object_permissions(request, story)
        request.data["story"] = story_id
        request.data["user"] = request.user.pk
        return super().post(request, *args, **kwargs)


class StoryCommentDetail(StoryCommentGeneric, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, StoryCommentAuthorOrReadOnly]

    def update_queryset(self, story_id, project_id):
        self.queryset = StoryComment.objects.filter(
            story__pk=story_id, story__project__pk=project_id
        )

    def get(self, request, project_id, story_id, pk, *args, **kwargs):
        self.update_queryset(story_id, project_id)
        return super().get(request, *args, **kwargs)

    def update(self, request, project_id, story_id, pk, *args, **kwargs):
        self.update_queryset(story_id, project_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, project_id, story_id, pk, *args, **kwargs):
        self.update_queryset(story_id, project_id)
        return super().destroy(request, *args, **kwargs)
