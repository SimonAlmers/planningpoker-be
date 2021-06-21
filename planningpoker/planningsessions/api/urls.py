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
    path(
        "projects/<uuid:project_id>/sessions/<uuid:session_id>/participants/heartbeat/",
        views.SessionParticipantHeartBeat.as_view(),
        name="session-participant-heartbeat",
    ),
    path(
        "projects/<uuid:project_id>/sessions/<uuid:session_id>/participants/exit/",
        views.SessionParticipantExit.as_view(),
        name="session-participant-exit",
    ),
]
