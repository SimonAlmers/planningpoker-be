from django.contrib import admin

from .models import Story, StoryComment


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "project",
        "status",
        "order",
        "requester",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["id", "created_at", "updated_at"]
    list_filter = ["status"]
    search_fields = ["project__id", "project__title", "title", "id"]


@admin.register(StoryComment)
class StoryCommentAdmin(admin.ModelAdmin):
    list_display = ["story", "user", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
