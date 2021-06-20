from django.shortcuts import get_object_or_404, render
from rest_framework import filters, generics, permissions, status
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from ..models import Project, ProjectMember
from .permissions import (
    ProjectIsMember,
    ProjectMemberIsMember,
    ProjectMemberIsProjectOwner,
    IsProjectOwner,
)
from .serializers import (
    ProjectListItemSerializer,
    ProjectMemberListSerializer,
    ProjectMemberDetailSerializer,
    ProjectSerializer,
)


class ProjectGeneric:
    permission_classes = [IsAuthenticated, ProjectIsMember]
    queryset = Project.objects.none()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(members__in=[user])
        return queryset


class ProjectList(ProjectGeneric, generics.ListCreateAPIView):
    serializer_class = ProjectListItemSerializer


class ProjectDetail(ProjectGeneric, generics.RetrieveUpdateDestroyAPIView):
    pass


class ProjectMemberGeneric:
    permission_classes = [IsAuthenticated, ProjectMemberIsMember]
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberDetailSerializer
    lookup_field = "id"


class ProjectMemberList(ProjectMemberGeneric, APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        self.check_object_permissions(self.request, project)

        data = request.data
        data["project_id"] = project_id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectMemberDetail(
    ProjectMemberGeneric, generics.UpdateAPIView, generics.DestroyAPIView
):
    permission_classes = [IsAuthenticated, ProjectMemberIsProjectOwner]
