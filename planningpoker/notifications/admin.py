from django.contrib import admin

from .models import Notification, SessionCommentNotificationData


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "kind",
        "read_at",
    ]
    readonly_fields = ["id"]


@admin.register(SessionCommentNotificationData)
class SessionCommentNotificationAdmin(admin.ModelAdmin):
    pass
