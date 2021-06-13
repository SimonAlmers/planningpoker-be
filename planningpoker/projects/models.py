import uuid as uuid_lib

from django.conf import settings
from django.db import models
from planningpoker.common.models import TimeStampedModel

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


class Project(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through="ProjectMember")

    objects = ProjectManager()

    def __str__(self):
        return self.title

    def get_members(self):
        """
        Returns related project members for the project.
        """
        return ProjectMember.objects.filter(project=self)



class ProjectMember(TimeStampedModel):
    VIEWER = 1
    MEMBER = 2
    OWNER = 3
    ROLE_CHOICES = [
        (VIEWER, "Viewer"),
        (MEMBER, "Member"),
        (OWNER, "Owner"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, default=MEMBER)

    class Meta:
        unique_together = ["project", "user"]

    def __str__(self):
        return str(self.user)
