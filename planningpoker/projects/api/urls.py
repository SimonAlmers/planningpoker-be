from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.ProjectList.as_view(), name="project-list"),
    path(
        "projects/<uuid:id>/",
        views.ProjectDetail.as_view(),
        name="project-detail",
    ),
    path(
        "projects/<uuid:project_id>/members/",
        views.ProjectMemberList.as_view(),
        name="project-member-list",
    ),
    path(
        "projects/<uuid:project_id>/members/<uuid:id>/",
        views.ProjectMemberDetail.as_view(),
        name="project-member-detail",
    ),
    path(
        "projects/<uuid:project_id>/invite_code/",
        views.ProjectInviteCodeDetail.as_view(),
        name="project-invite-code-detail",
    ),
    path(
        "projects/join/",
        views.AcceptInviteCode.as_view(),
        name="accept-project-invite",
    ),
]
