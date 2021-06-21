from django.urls import path

from . import views

urlpatterns = [
    path(
        "notifications/<uuid:id>/mark_read",
        views.NotificationDetail.as_view(),
        name="notification-detail",
    ),
]
