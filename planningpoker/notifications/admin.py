from django.contrib import admin
from .models import Notification, SessionCommentNotificationData

# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]


@admin.register(SessionCommentNotificationData)
class SessionCommentNotificationAdmin(admin.ModelAdmin):
    pass