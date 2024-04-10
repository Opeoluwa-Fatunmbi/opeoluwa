from django.contrib import admin
from .models import SiteDetail, Message


class SiteDetailAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")
    list_filter = list_display


admin.site.register(SiteDetail, SiteDetailAdmin)
admin.site.register(Message, MessageAdmin)
