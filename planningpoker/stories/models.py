from common.models import TimeStampedModel
from django.conf import settings
from django.db import models
from projects.models import Project

# Create your models here.


# class StoryManager(models.Manager):


#     def get_first_story(self, project_id):
#         return Story.objects.get(project__pk=project_id, prev_story=None)

#     def get_last_story(self, project_id):
#         return Story.objects.get(project__pk=project_id, next_story=None)

#     def get_next_story(self, story):
#         return story.next_story

#     def get_previous_story(self, story):
#         return story.prev_story

#     def move_to_first(self, story):
#         """
#         Takes a story that should be moved to start of project.

#         - Sets `prev_story` on passed story to `None`
#         - Sets `next_story` on passed story to current `first story`
#         - Sets passed story as current first story's `prev_story`
#         """
#         first_story = self.get_first_story(story.project.id)

#         story.prev_story = None
#         story.next_story = first_story
#         story.save()

#         first_story.prev_story = story
#         first_story.save()
#         return story

#     def reorder_story(self, story, before_story, after_story):
#         story_was_first = story.prev_story == None
#         story_was_last = story.next_story == None

#         if before_story == after_story:
#             raise Exception("The before_story and after_story can NOT be the same!")

#         if before_story is not None and after_story is None:
#             print("MOVE TO START!")
#             return self.move_to_first(story)

#         if before_story is None and after_story is not None:
#             print("MOVE TO END!")

#         if before_story and after_story:
#             print("MOVE TO INBETWEEN!")

#         story.before_story = None
#         story.after_story = None
#         story.save()

#         return story


class Story(TimeStampedModel):
    POINT_SCALE = [
        (0, "Pass"),
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 5),
        (8, 8),
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

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    score = models.IntegerField(choices=POINT_SCALE, blank=True, null=True)
    kind = models.IntegerField(choices=KIND_CHOICES, default=FEATURE)
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="requester",
        null=True,
        blank=True,
    )
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNSCHEDULED)
    next_story = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="_next_story",
        blank=True,
        null=True,
    )
    prev_story = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="_previous_story",
        blank=True,
        null=True,
    )

    # objects = StoryManager()

    class Meta:
        verbose_name_plural = "Stories"
        ordering = ["-status"]

    def __str__(self):
        return self.title


class StoryComment(TimeStampedModel):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    text = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE)


