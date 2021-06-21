from django.shortcuts import render
from rest_framework import filters, generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Project, ProjectInviteCode, ProjectMember
from .permissions import (
    IsProjectOwner,
    ProjectIsMember,
    ProjectMemberIsMember,
    ProjectMemberIsProjectOwner,
)
from .serializers import (
    ProjectInviteCodeSerialiser,
    ProjectListItemSerializer,
    ProjectMemberDetailSerializer,
    ProjectMemberListSerializer,
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
    queryset = ProjectMember.objects.none()
    serializer_class = ProjectMemberDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return ProjectMember.objects.filter(project__id=project_id)


class ProjectMemberList(ProjectMemberGeneric, generics.ListCreateAPIView):
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


class ProjectInviteCodeDetail(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, project_id, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        project = Project.objects.get(id=project_id)
        invite_code, created = ProjectInviteCode.objects.get_or_create(project=project)
        serializer = ProjectInviteCodeSerialiser(invite_code)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcceptInviteCode(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        invite_code = request.data["invite_code"]
        try:
            invite = ProjectInviteCode.objects.get(id=invite_code)
            if invite is not None and invite.is_valid():
                ProjectMember.objects.get_or_create(
                    user=request.user, project=invite.project
                )
                return Response(
                    {"project_id": str(invite.project.id)}, status.HTTP_200_OK
                )

            return Response(
                {"message": "The invite has expired!"}, status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {"message": "The invite has expired!"}, status.HTTP_400_BAD_REQUEST
            )
