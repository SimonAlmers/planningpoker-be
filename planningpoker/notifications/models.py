from common.models import TimeStampedModel, UUIDModel
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete
from planningsessions.models import PlanningSessionComment

from .tasks.firebase import FirebaseNotification


class Notification(UUIDModel, TimeStampedModel):
    SYSTEM = 0
    PROJECT_INVITE = 1
    SESSION_INVITE = 2
    SESSION_COMMENT_MENTION = 3
    STORY_COMMENT_MENTION = 4
    STORY_UPDATE = 5
    KIND_CHOICES = [
        (SYSTEM, "System Notification"),
        (PROJECT_INVITE, "Project Invite"),
        (SESSION_INVITE, "Session Invite"),
        (SESSION_COMMENT_MENTION, "Session Comment Mention"),
        (STORY_COMMENT_MENTION, "Story Comment Mention"),
        (STORY_UPDATE, "Story Update"),
    ]
    kind = models.IntegerField(choices=KIND_CHOICES)
    message = models.CharField(max_length=128)
    context = models.CharField(max_length=128)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="id",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="id",
        related_name="notifications",
        on_delete=models.CASCADE,
    )
    read_at = models.DateTimeField(blank=True, null=True)


class SessionCommentNotificationData(models.Model):
    notification = models.OneToOneField(
        Notification,
        primary_key=True,
        to_field="id",
        related_name="session_comment",
        on_delete=models.CASCADE,
    )
    comment = models.ForeignKey(
        PlanningSessionComment, to_field="id", on_delete=models.CASCADE
    )


def notification_post_save(sender, instance, created, **kwargs):
    firebase = FirebaseNotification()
    firebase.update_notification(instance)


def notification_pre_delete(sender, instance, **kwargs):
    firebase = FirebaseNotification()
    firebase.delete_notification(instance)


post_save.connect(notification_post_save, sender=Notification)
pre_delete.connect(notification_pre_delete, sender=Notification)
