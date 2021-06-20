from common.models import TimeStampedModel, UUIDModel
from django.db import models
from projects.models import Project
from stories.models import Story
from django.conf import settings


class PlanningSession(UUIDModel, TimeStampedModel):
    project = models.ForeignKey(Project, to_field="id", on_delete=models.CASCADE)
    stories = models.ManyToManyField(Story, blank=True)
    focused_story = models.ForeignKey(
        Story,
        to_field="id",
        related_name="focused_story",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # Notify Project.members when session is created


class PlanningSessionParticipant(UUIDModel, TimeStampedModel):
    session = models.ForeignKey(PlanningSession, to_field="id", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="id", on_delete=models.CASCADE)
    last_seen = models.DateTimeField(blank=True, null=True)
    last_exit = models.DateTimeField(blank=True, null=True)

    # Update to keep alive


class PlanningSessionComment(UUIDModel, TimeStampedModel):
    parent = models.ForeignKey("self", to_field="id", blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="id", on_delete=models.PROTECT)
    text = models.TextField()
    session = models.ForeignKey(PlanningSession, to_field="id", on_delete=models.CASCADE)


class Vote(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="id", on_delete=models.CASCADE)
    story = models.ForeignKey(Story, to_field="id", on_delete=models.CASCADE)
    point = models.IntegerField(choices=Story.POINT_SCALE)

    class Meta:
        unique_together = ["user", "story"]
