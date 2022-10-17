from django.contrib import admin

from clients.models import clients


@admin.register(clients.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'dob',
    )
    list_display_links = ('first_name',)
