from common.models import TimeStampedModel, UUIDModel
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete
from projects.models import Project
from stories.models import Story


from .tasks.firebase import (
    FirebasePlanningSession,
    FirebasePlanningSessionComment,
    FirebasePlanningSessionParticipant,
    FirebaseVote,
)


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

    def collect_unestimated_stories(self):
        stories = Story.objects.filter(project=self.project, score=None)
        self.focused_story = stories.first()
        self.stories.set(stories)
        self.save()

    def notify_all_members(self):
        from notifications.models import Notification, SessionInviteNotificationData

        members = self.project.projectmember_set.all()
        for member in members:
            notification = Notification.objects.create(
                kind=2,
                message="Someone Created a Session",
                context="Join the planning session now!",
                sender=None,
                user=member.user,
            )
            SessionInviteNotificationData.objects.create(notification=notification, session=self)


class PlanningSessionParticipant(UUIDModel, TimeStampedModel):
    session = models.ForeignKey(
        PlanningSession, to_field="id", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, to_field="id", on_delete=models.CASCADE
    )
    last_seen = models.DateTimeField(blank=True, null=True)
    last_exit = models.DateTimeField(blank=True, null=True)

    # Update to keep alive


class PlanningSessionComment(UUIDModel, TimeStampedModel):
    parent = models.ForeignKey(
        "self", to_field="id", blank=True, null=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, to_field="id", on_delete=models.PROTECT
    )
    text = models.TextField()
    session = models.ForeignKey(
        PlanningSession, to_field="id", on_delete=models.CASCADE
    )


class Vote(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, to_field="id", on_delete=models.CASCADE
    )
    story = models.ForeignKey(Story, to_field="id", on_delete=models.CASCADE)
    point = models.IntegerField(choices=Story.POINT_SCALE)

    class Meta:
        unique_together = ["user", "story"]


# SIGNALS


def planningsession_post_save(sender, instance, created, **kwargs):
    if created:
        instance.collect_unestimated_stories()
        instance.notify_all_members()
    firebase = FirebasePlanningSession()
    firebase.update_session(instance)


def planningsession_pre_delete(sender, instance, **kwargs):
    firebase = FirebasePlanningSession()
    firebase.delete_session(instance)


def planningsession_comment_post_save(sender, instance, created, **kwargs):
    firebase = FirebasePlanningSessionComment()
    firebase.update_comment(instance)


def planningsession_comment_pre_delete(sender, instance, **kwargs):
    firebase = FirebasePlanningSessionComment()
    firebase.delete_comment(instance)


def planningsession_participant_post_save(sender, instance, created, **kwargs):
    firebase = FirebasePlanningSessionParticipant()
    firebase.update_participant(instance)


def planningsession_participant_pre_delete(sender, instance, **kwargs):
    firebase = FirebasePlanningSessionParticipant()
    firebase.delete_participant(instance)


def vote_post_save(sender, instance, created, **kwargs):
    firebase = FirebaseVote()
    firebase.update_vote(instance)


def vote_pre_delete(sender, instance, **kwargs):
    firebase = FirebaseVote()
    firebase.delete_vote(instance)


post_save.connect(planningsession_post_save, sender=PlanningSession)
pre_delete.connect(planningsession_pre_delete, sender=PlanningSession)
post_save.connect(planningsession_comment_post_save, sender=PlanningSessionComment)
pre_delete.connect(planningsession_comment_pre_delete, sender=PlanningSessionComment)
post_save.connect(
    planningsession_participant_post_save, sender=PlanningSessionParticipant
)
pre_delete.connect(
    planningsession_participant_pre_delete, sender=PlanningSessionParticipant
)
post_save.connect(vote_post_save, sender=Vote)
pre_delete.connect(vote_pre_delete, sender=Vote)
