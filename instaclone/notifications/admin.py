from django.contrib import admin
from . import models

@admin.register(models.Notifications)
class NotificationAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'to',
        'notifications_type'

    )