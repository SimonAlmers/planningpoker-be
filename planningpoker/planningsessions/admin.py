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
    readonly_fields = ["id"]


@admin.register(PlanningSessionParticipant)
class PlanningSessionParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(PlanningSessionComment)
class PlanningSessionCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
