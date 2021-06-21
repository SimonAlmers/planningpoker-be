from django.urls import path

from . import views

urlpatterns = [
    path(
        "projects/<uuid:project_id>/sessions/",
        views.PlanningSessionList.as_view(),
        name="planningsession-list",
    ),
    path(
        "projects/<uuid:project_id>/sessions/<uuid:id>/",
        views.PlanningSessionDetail.as_view(),
        name="planningsession-detail",
    ),
    path(
        "projects/<uuid:project_id>/sessions/<uuid:session_id>/comments/",
        views.PlanningSessionCommentList.as_view(),
        name="planningsession-comment-list",
    ),
    path(
        "projects/<uuid:project_id>/sessions/<uuid:session_id>/comments/<uuid:id>/",
        views.PlanningSessionCommentDetail.as_view(),
        name="planningsession-comment-detail",
    ),
    path(
        "projects/<uuid:project_id>/stories/<uuid:story_id>/votes/",
        views.StoryVoteList.as_view(),
        name="story-vote-list",
    ),
    path(
        "projects/<uuid:project_id>/stories/<uuid:story_id>/votes/<uuid:id>/",
        views.StoryVoteDetail.as_view(),
        name="story-vote-detail",
    ),
    # "projects/:project_id/sessions/:session_id/participants/"
    # "projects/:project_id/sessions/:session_id/participants/:uuid/"
    # "projects/:project_id/sessions/:session_id/participants/:uuid/heartbeat/"
    # "projects/:project_id/sessions/:session_id/participants/:uuid/leave/"
]
