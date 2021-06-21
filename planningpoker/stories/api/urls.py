from django.urls import path

from . import views

urlpatterns = [
    path(
        "projects/<uuid:project_id>/stories/",
        views.StoryList.as_view(),
        name="story-list",
    ),
    path(
        "projects/<uuid:project_id>/stories/reorder/",
        views.StoryReorder.as_view(),
        name="story-list-reorder",
    ),
    path(
        "projects/<uuid:project_id>/stories/<uuid:id>/",
        views.StoryDetail.as_view(),
        name="story-detail",
    ),
    path(
        "projects/<uuid:project_id>/stories/<uuid:story_id>/comments/",
        views.StoryCommentList.as_view(),
        name="story-comment-list",
    ),
    path(
        "projects/<uuid:project_id>/stories/<uuid:story_id>/comments/<uuid:id>/",
        views.StoryCommentDetail.as_view(),
        name="story-comment-detail",
    ),
]
