from django.contrib import admin

from .models import (
    PlanningSession,
    PlanningSessionComment,
    PlanningSessionParticipant,
    Vote,
)

# Register your models here.


@admin.register(PlanningSession)
class PlanningSessionAdmin(admin.ModelAdmin):
    list_display = ["project", "focused_story"]
    readonly_fields = ["id"]


@admin.register(PlanningSessionParticipant)
class PlanningSessionParticipantAdmin(admin.ModelAdmin):
    list_display = ["user", "session", "created_at", "last_seen"]


@admin.register(PlanningSessionComment)
class PlanningSessionCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "session", "created_at"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "point", "story", "created_at"]
