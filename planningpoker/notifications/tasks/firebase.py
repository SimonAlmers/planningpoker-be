import datetime

from django.conf import settings
from firebase_admin import credentials, db, get_app
from rest_framework import serializers


class FirebaseNotification:
    def __init__(self):
        self.app = get_app(name=settings.FIREBASE_NAME)

    def get_notification_ref(self, notification):
        DB_REF = db.reference(
            f"users/{notification.user.id}/notifications", app=self.app
        )
        ref = DB_REF.child(f"{notification.id}")
        return ref

    def update_notification(self, notification):
        ref = self.get_notification_ref(notification)
        ref.set(
            {
                "id": str(notification.id),
                "kind": notification.kind,
                "sender": str(notification.sender),
                "message": str(notification.message),
                "context": str(notification.context),
                "readAt": str(notification.read_at),
                "createdAt": str(notification.created_at),
                "updatedAt": str(notification.updated_at),
            }
        )
    
    def update_session_invite(self, session_invite):
        session = session_invite.session
        notification = session_invite.notification
        ref = self.get_notification_ref(notification)
        ref.set(
            {
                "id": str(notification.id),
                "kind": notification.kind,
                "sender": str(notification.sender),
                "message": str(notification.message),
                "context": str(notification.context),
                "readAt": str(notification.read_at),
                "createdAt": str(notification.created_at),
                "updatedAt": str(notification.updated_at),
                "sessionId": str(session.id),
                "projectId": str(session.project.id),
            }
        )

    def delete_notification(self, notification):
        ref = self.get_notification_ref(notification)
        ref.delete()
