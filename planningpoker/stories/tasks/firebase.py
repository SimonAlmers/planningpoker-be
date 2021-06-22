from django.conf import settings
from firebase_admin import credentials, db, get_app


class FirebaseStoryComment:
    def __init__(self):
        self.app = get_app(name=settings.FIREBASE_NAME)

    def get_comment_ref(self, comment):
        DB_REF = db.reference(
            f"projects/{comment.story.project.id}/stories/{comment.story.id}/comments",
            app=self.app,
        )
        ref = DB_REF.child(f"{comment.id}")
        return ref

    def update_comment(self, comment):
        ref = self.get_comment_ref(comment)

        ref.set(
            {
                "id": str(comment.id),
                "parent": str(comment.parent),
                "user": {
                    "id": str(comment.user.id),
                    "initials": comment.user.get_initials(),
                    "firstName": comment.user.first_name,
                    "lastName": comment.user.last_name,
                },
                "text": comment.text,
                "createdAt": str(comment.created_at),
                "updatedAt": str(comment.updated_at),
            }
        )

    def delete_comment(self, comment):
        ref = self.get_comment_ref(comment)
        ref.delete()
