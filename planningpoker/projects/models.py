import uuid as uuid_lib
import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from common.models import TimeStampedModel, UUIDModel

# Create your models here.


class ProjectManager(models.Manager):
    def create_project(self, user, title, description=None):
        """
        Creates an returns a project and assign a user as project owner.
        """
        project = self.create(title=title, description=description)
        ProjectMember.objects.create(
            project=project, user=user, role=ProjectMember.OWNER
        )
        return project


class Project(UUIDModel, TimeStampedModel):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through="ProjectMember")

    objects = ProjectManager()

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def create_invite_code(self):
        invite = ProjectInviteCode.objects.create(project=self)
        return invite

    def get_members(self):
        """
        Returns related project members for the project.
        """
        return ProjectMember.objects.filter(project=self)

    def get_stories(self):
        from stories.models import Story

        return Story.objects.filter(project=self)


class ProjectInviteCode(UUIDModel, TimeStampedModel):
    project = models.OneToOneField(
        Project,
        to_field="id",
        related_name="invite_code",
        on_delete=models.CASCADE,
    )

    def is_valid(self):
        now = timezone.now()
        diff = now - self.created_at
        days = diff.days
        return days < 1

    def expires_at(self):
        expires_at = self.created_at + datetime.timedelta(days=1)
        return expires_at


class ProjectMember(UUIDModel, TimeStampedModel):
    VIEWER = 1
    MEMBER = 2
    OWNER = 3
    ROLE_CHOICES = [
        (VIEWER, "Viewer"),
        (MEMBER, "Member"),
        (OWNER, "Owner"),
    ]

    project = models.ForeignKey(Project, to_field="id", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, to_field="id", on_delete=models.CASCADE
    )
    role = models.IntegerField(choices=ROLE_CHOICES, default=MEMBER)

    class Meta:
        unique_together = ["project", "user"]

    def __str__(self):
        return str(self.user)
