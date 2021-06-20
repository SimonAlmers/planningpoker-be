import random
from users.models import User
from common.obfuscater import Obfuscater


class UserFactory:
    @classmethod
    def create(cls, *args, **kwargs):
        return User.objects.create(*args, **kwargs)

    @classmethod
    def create_test_user(cls):
        first_name = Obfuscater.first_name()
        last_name = Obfuscater.last_name()
        email = Obfuscater.email(first_name, last_name)
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "is_active": True,
        }
        user = cls.create(**data)
        return user
