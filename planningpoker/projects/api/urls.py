from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.ProjectList.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/",
        views.ProjectDetail.as_view(),
        name="project-detail",
    ),
    path(
        "projects/<int:project_id>/members/",
        views.ProjectMemberList.as_view(),
        name="project-member-list",
    ),
    path(
        "projects/<int:project_id>/members/<int:pk>/",
        views.ProjectMemberDetail.as_view(),
        name="project-member-detail",
    ),
]
