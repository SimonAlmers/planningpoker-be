from common.models import TimeStampedModel, UUIDModel
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete
from planningsessions.models import PlanningSessionComment, PlanningSession

from stories.models import Story, StoryComment
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




class SystemNotificationData(models.Model):
     notification = models.OneToOneField(
        Notification,
        primary_key=True,
        to_field="id",
        related_name="system",
        on_delete=models.CASCADE,
    )


class ProjectInviteNotificationData(models.Model):
    notification = models.OneToOneField(
        Notification,
        primary_key=True,
        to_field="id",
        related_name="project_invite",
        on_delete=models.CASCADE,
    )
    # invite = models.ForeignKey(, to_field="id", on_delete=models.CASCADE)


class SessionInviteNotificationData(models.Model):
    notification = models.OneToOneField(
        Notification,
        primary_key=True,
        to_field="id",
        related_name="session_invite",
        on_delete=models.CASCADE,
    )
    session = models.ForeignKey(PlanningSession, to_field="id", on_delete=models.CASCADE)



class StoryCommentNotificationData(models.Model):
    notification = models.OneToOneField(
        Notification,
        primary_key=True,
        to_field="id",
        related_name="story_comment",
        on_delete=models.CASCADE,
    )
    comment = models.ForeignKey(StoryComment, to_field="id", on_delete=models.CASCADE)

class StoryNotificationData(models.Model):
    notification = models.OneToOneField(
        Notification,
        primary_key=True,
        to_field="id",
        related_name="story",
        on_delete=models.CASCADE,
    )
    story = models.ForeignKey(Story, to_field="id", on_delete=models.CASCADE)



def session_invite_post_save(sender, instance, created, **kwargs):
    firebase = FirebaseNotification()
    firebase.update_session_invite(instance)


def session_invite_pre_delete(sender, instance, **kwargs):
    firebase = FirebaseNotification()
    firebase.delete_notification(instance.notification)


def notification_post_save(sender, instance, created, **kwargs):
    firebase = FirebaseNotification()
    firebase.update_notification(instance)


def notification_pre_delete(sender, instance, **kwargs):
    firebase = FirebaseNotification()
    firebase.delete_notification(instance)




post_save.connect(session_invite_post_save, sender=SessionInviteNotificationData)
pre_delete.connect(session_invite_pre_delete, sender=SessionInviteNotificationData)

post_save.connect(notification_post_save, sender=Notification)
pre_delete.connect(notification_pre_delete, sender=Notification)
