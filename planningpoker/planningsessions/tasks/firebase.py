from django.conf import settings
from firebase_admin import db, credentials, get_app
import datetime
from rest_framework import serializers


from django.conf import settings
from firebase_admin import db, credentials, get_app
import datetime


class FirebaseVote:
    def __init__(self):
        self.app = get_app(name=settings.FIREBASE_NAME)

    def get_vote_ref(self, vote):
        DB_REF = db.reference(
            f"projects/{vote.story.project.id}/stories/{vote.story.id}/votes",
            app=self.app,
        )
        ref = DB_REF.child(f"{vote.id}")
        return ref

    def update_vote(self, vote):
        ref = self.get_vote_ref(vote)

        ref.set(
            {
                "user": str(vote.user.id),
                "story": str(vote.story.id),
                "point": vote.point,
                "created_at": str(vote.created_at),
                "updated_at": str(vote.updated_at),
            }
        )

    def delete_vote(self, vote):
        ref = self.get_vote_ref(vote)
        ref.delete()


class FirebasePlanningSession:
    def __init__(self):
        self.app = get_app(name=settings.FIREBASE_NAME)

    def get_session_ref(self, session):
        DB_REF = db.reference(f"projects/{session.project.id}/sessions", app=self.app)
        ref = DB_REF.child(f"{session.id}/focusedStory")
        return ref

    def update_session(self, session):
        ref = self.get_session_ref(session)

        focused_story = "None"
        if session.focused_story is not None:
            focused_story = str(session.focused_story)

        ref.set(focused_story)

    def delete_session(self, session):
        ref = self.get_session_ref(session)
        ref.delete()


class FirebasePlanningSessionParticipant:
    def __init__(self):
        self.app = get_app(name=settings.FIREBASE_NAME)

    def get_participant_ref(self, participant):
        DB_REF = db.reference(
            f"projects/{participant.session.project.id}/sessions", app=self.app
        )
        ref = DB_REF.child(f"{participant.session.id}/participants/{participant.id}")
        return ref

    def update_participant(self, participant):
        ref = self.get_participant_ref(participant)
        ref.set(
            {
                "user": str(participant.user),
                "lastSeen": str(participant.last_seen),
                "lastExit": str(participant.last_exit),
            }
        )

    def delete_participant(self, participant):
        ref = self.get_participant_ref(participant)
        ref.delete()


class FirebasePlanningSessionComment:
    def __init__(self):
        self.app = get_app(name=settings.FIREBASE_NAME)

    def get_comment_ref(self, comment):
        DB_REF = db.reference(
            f"projects/{comment.session.project.id}/sessions/{comment.session.id}/comments",
            app=self.app,
        )
        ref = DB_REF.child(f"{comment.id}")
        return ref

    def update_comment(self, comment):
        ref = self.get_comment_ref(comment)

        ref.set(
            {
                "parent": str(comment.parent),
                "user": str(comment.user),
                "text": comment.text,
            }
        )

    def delete_comment(self, comment):
        ref = self.get_comment_ref(comment)
        ref.delete()
