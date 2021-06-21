import uuid

from common.models import TimeStampedModel, UUIDModel
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, UUIDModel, TimeStampedModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_initials(self):
        """
        Returns the first letter of the first_name and last_name in uppercase.
        """
        initials = f"{self.first_name[0]}{self.last_name[0]}".upper()
        return initials

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
