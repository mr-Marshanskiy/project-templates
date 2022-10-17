from django.contrib import admin

from events.models import events


@admin.register(events.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_start',
        'date_end',
    )
    list_display_links = ('name',)
