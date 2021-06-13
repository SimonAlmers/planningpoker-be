from django.contrib import admin

from .models import Story, StoryComment

# Register your models here.


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "project",
        "status",
        "requester",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["created_at", "updated_at"]
    list_filter = ["status"]


@admin.register(StoryComment)
class StoryCommentAdmin(admin.ModelAdmin):
    list_display = ["story", "user", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
