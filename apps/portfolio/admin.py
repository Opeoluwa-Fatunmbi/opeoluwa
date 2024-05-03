from django.contrib import admin
from apps.portfolio.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    list_filter = list_display
    search_fields = ["name"]


admin.site.register(Project, ProjectAdmin)