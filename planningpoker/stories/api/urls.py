from django.urls import path
from . import views

urlpatterns = [
    path(
        "projects/<int:project_id>/stories/",
        views.StoryList.as_view(),
        name="story-list",
    ),
    path(
        "projects/<int:project_id>/stories/reorder/",
        views.StoryReorder.as_view(),
        name="story-list-reorder",
    ),
    path(
        "projects/<int:project_id>/stories/<int:pk>/",
        views.StoryDetail.as_view(),
        name="story-detail",
    ),
    path(
        "projects/<int:project_id>/stories/<int:story_id>/comments/",
        views.StoryCommentList.as_view(),
        name="story-comment-list",
    ),
    path(
        "projects/<int:project_id>/stories/<int:story_id>/comments/<int:pk>/",
        views.StoryCommentDetail.as_view(),
        name="story-comment-detail",
    ),
]
