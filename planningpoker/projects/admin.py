from django.contrib import admin
from django.db.models import Count

from .models import Project, ProjectMember

# Register your models here.


class ProjectMemberInline(admin.TabularInline):
    model = Project.members.through


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "member_count", "created_at", "updated_at"]
    readonly_fields = ["uuid", "created_at", "updated_at"]
    inlines = [ProjectMemberInline]
    search_fields = ["uuid", "title"]

    def member_count(self, obj):
        return obj.member_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(member_count=Count("members"))
        return queryset
