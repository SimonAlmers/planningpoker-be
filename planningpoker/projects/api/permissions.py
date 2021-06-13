from rest_framework.permissions import SAFE_METHODS, BasePermission

from ..models import ProjectMember


class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        member = obj.get_members().filter(
            role=ProjectMember.OWNER, project=obj, user=user
        )

        return member.exists()


class IsProjectMemberOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        member = obj.get_members().filter(user=user, project=obj).first()

        if request.method in SAFE_METHODS:
            return member is not None
        else:
            return member is not None and member.role >= ProjectMember.MEMBER


class ProjectIsMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        member = obj.get_members().get(user=user)

        if request.method in SAFE_METHODS:
            return member is not None
        elif request.method == "DELETE":
            return member.role == ProjectMember.OWNER
        else:
            return member.role >= ProjectMember.MEMBER


class ProjectMemberIsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        project = obj.project
        member = project.get_members().filter(
            role=ProjectMember.OWNER, project=project, user=user
        )

        return member.exists()


class ProjectMemberIsMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        project = obj.project
        member = project.get_members().filter(user=user)
        return member.exists()

    def has_permission(self, request, view):
        user = request.user
        try:
            project_id = view.kwargs["project_id"]
            member = ProjectMember.objects.filter(project__pk=project_id, user=user)

            return member.exists()
        except KeyError:
            return True
