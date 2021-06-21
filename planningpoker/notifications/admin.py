from django.contrib import admin

from .models import ( Notification, SessionCommentNotificationData,
SystemNotificationData,
ProjectInviteNotificationData,
SessionInviteNotificationData,
StoryCommentNotificationData,
StoryNotificationData,
)


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

@admin.register(SystemNotificationData)
class SystemNotificationDataAdmin(admin.ModelAdmin):
    pass 


@admin.register(ProjectInviteNotificationData)
class ProjectInviteNotificationDataAdmin(admin.ModelAdmin):
    pass 


@admin.register(SessionInviteNotificationData)
class SessionInviteNotificationDataAdmin(admin.ModelAdmin):
    pass 


@admin.register(StoryCommentNotificationData)
class StoryCommentNotificationDataAdmin(admin.ModelAdmin):
    pass 


@admin.register(StoryNotificationData)
class StoryNotificationDataAdmin(admin.ModelAdmin):
    pass 


