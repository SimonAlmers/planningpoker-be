from projects.models import ProjectMember
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsSessionProjectMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        project = obj.project
        member = project.get_members().filter(user=user, project=project).first()

        if request.method in SAFE_METHODS:
            return member is not None

        return member is not None and member.role >= ProjectMember.MEMBER


class SessionCommentAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        comment = obj
        project = comment.session.project
        member = project.get_members().filter(user=user, project=project).first()

        if request.method in SAFE_METHODS:
            return member is not None
        else:
            return comment.user == user


class VoteOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        vote = obj
        project = vote.story.project
        member = project.get_members().filter(user=user, project=project).first()

        if request.method in SAFE_METHODS:
            return member is not None
        else:
            return vote.user == user
