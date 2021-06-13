from rest_framework import serializers
from ..models import Story, StoryComment


class StoryReorderSerializer(serializers.Serializer):
    story = serializers.IntegerField()
    before_story = serializers.IntegerField()
    after_story = serializers.IntegerField()

    class Meta:
        fields = [
            "story",
            "before_story",
            "after_story",
        ]


class StoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    comments = StoryCommentSerializer(
        many=True, source="storycomment_set", read_only=True
    )

    class Meta:
        model = Story
        fields = "__all__"
