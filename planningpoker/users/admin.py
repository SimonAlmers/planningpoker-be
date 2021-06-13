from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ["uid"]
    list_display = [
        "email",
        "first_name",
        "last_name",
        "created_at",
        "updated_at",
        "is_active",
        "is_staff",
        "is_admin",
    ]
    list_filter = [
        "is_active",
        "is_staff",
        "is_admin",
    ]
    search_fields = [
        "email",
        "uid",
        "first_name",
        "last_name",
    ]
