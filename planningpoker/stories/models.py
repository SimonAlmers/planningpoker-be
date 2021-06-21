from common.models import TimeStampedModel, UUIDModel
from bulk_update.helper import bulk_update
from django.conf import settings
from django.db import models
from projects.models import Project


class StoryManager(models.Manager):
    def create_story(self, user, project, title, description=None):
        """
        Creates an returns a story and assign a user as story requester.
        """
        order = 0
        last_story = self.get_last_story_for_project(project.id)
        if last_story is not None:
            order = last_story.order + 1
        story = self.create(
            title=title,
            description=description,
            requester=user,
            project=project,
            order=order,
        )
        return story

    def get_last_story_for_project(self, project_id):
        return Story.objects.filter(project__id=project_id).order_by("order").last()


class Story(UUIDModel, TimeStampedModel):
    POINT_SCALE = [
        (0, "Pass"),
        (1, "1/2"),
        (2, "1"),
        (3, "2"),
        (4, "3"),
        (5, "5"),
        (6, "8"),
        (7, "13"),
    ]

    FEATURE = 1
    BUG = 2
    RELEASE = 3
    KIND_CHOICES = [
        (FEATURE, "Feature"),
        (BUG, "Bug"),
        (RELEASE, "Release"),
    ]

    UNSCHEDULED = 0
    BACKLOG = 1
    STARTED = 2
    FINISHED = 3
    TESTED = 4
    ACCEPTED = 5
    REJECTED = 6
    DEPLOYED = 7

    STATUS_CHOICES = [
        (UNSCHEDULED, "Unscheduled"),
        (BACKLOG, "Backlog"),
        (STARTED, "Started"),
        (FINISHED, "Finished"),
        (TESTED, "Tested"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
        (DEPLOYED, "Deployed"),
    ]

    project = models.ForeignKey(Project, to_field="id", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    score = models.IntegerField(choices=POINT_SCALE, blank=True, null=True)
    kind = models.IntegerField(choices=KIND_CHOICES, default=FEATURE)
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="id",
        on_delete=models.SET_NULL,
        related_name="requester",
        null=True,
        blank=True,
    )
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNSCHEDULED)
    order = models.IntegerField(blank=True, null=True)

    objects = StoryManager()

    class Meta:
        verbose_name_plural = "Stories"
        ordering = ["-status", "order"]

    def __str__(self):
        return self.title

    def move_to_index(self, index):
        """
        This function sets the story's order to the specified index and updates any affected stories.
        """
        print(f"Move to INDEX: {index}!")
        if self.order > index:
            stories = Story.objects.filter(
                project=self.project, order__lt=self.order, order__gte=index
            )
            start_value = index + 1
        else:
            stories = Story.objects.filter(
                project=self.project, order__lte=index, order__gt=self.order
            )
            start_value = self.order

        for order, story in enumerate(stories, start=start_value):
            story.order = order
        bulk_update(stories)
        self.order = index
        self.save()

    def move_to_start(self):
        """
        This function updated the story's order to the specified index and updates any affected stories.
        """
        self.move_to_index(0)

    def move_to_end(self):
        """
        This function updated the story's order to 1 greater than the order of the currently last story.
        No other stories are updated for performance reasons.
        """
        print("Move to END!")
        last_story = Story.objects.get_last_story_for_project(self.project.id)
        self.order = last_story.order + 1
        self.save()


class StoryComment(UUIDModel, TimeStampedModel):
    parent = models.ForeignKey(
        "self", to_field="id", blank=True, null=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, to_field="id", on_delete=models.PROTECT
    )
    text = models.TextField()
    story = models.ForeignKey(Story, to_field="id", on_delete=models.CASCADE)
