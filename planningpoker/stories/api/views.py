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
    lookup_field = "id"


class StoryList(StoryGeneric, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsProjectMemberOrReadOnly]

    def get(self, request, project_id, *args, **kwargs):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        self.queryset = Story.objects.filter(project__id=project_id)
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, *args, **kwargs):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        request.data["project_id"] = project_id
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
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(request, project)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            story_id = serializer.validated_data.get("story")
            index = serializer.validated_data.get("index")
            story = Story.objects.get(id=story_id)
            data = serializer.data
            last_story = Story.objects.get_last_story_for_project(story.project.id)
            if index >= last_story.order:
                story.move_to_end()
                data["index"] = last_story.order + 1
            else:
                story.move_to_index(index)
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoryCommentGeneric:
    permission_classes = [IsAuthenticated, StoryPermissionIsMemberOrReadOnly]
    serializer_class = StoryCommentSerializer
    queryset = StoryComment.objects.none()
    lookup_field = "id"


class StoryCommentList(StoryCommentGeneric, generics.ListCreateAPIView):
    def get(self, request, project_id, story_id, *args, **kwargs):
        story = Story.objects.get(id=story_id)
        self.check_object_permissions(request, story)

        self.queryset = StoryComment.objects.filter(
            story__id=story_id, story__project__id=project_id
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, project_id, story_id, *args, **kwargs):
        story = Story.objects.get(id=story_id)
        self.check_object_permissions(request, story)
        request.data["story"] = story_id
        request.data["user_id"] = request.user.id
        return super().post(request, *args, **kwargs)


class StoryCommentDetail(StoryCommentGeneric, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, StoryCommentAuthorOrReadOnly]

    def update_queryset(self, story_id, project_id):
        self.queryset = StoryComment.objects.filter(
            story__id=story_id, story__project__id=project_id
        )

    def get(self, request, project_id, story_id, id, *args, **kwargs):
        self.update_queryset(story_id, project_id)
        return super().get(request, *args, **kwargs)

    def update(self, request, project_id, story_id, id, *args, **kwargs):
        self.update_queryset(story_id, project_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, project_id, story_id, id, *args, **kwargs):
        self.update_queryset(story_id, project_id)
        return super().destroy(request, *args, **kwargs)
