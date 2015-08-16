from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Event, EventsConfig
from sorl.thumbnail.admin import AdminImageMixin
from solo.admin import SingletonModelAdmin

# Register your models here.
@admin.register(Event)
class EventAdmin(AdminImageMixin, PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                'from_datetime',
                'to_datetime',
                'excerpt',
                'content',
                'main_image',
            ]
        }),
        ('Contact Information', {
            'fields': [
                'event_contact',
                'extra_contact_information',
            ]
        }),
        ('Event Location', {
            'fields': [
                'location_name',
                'address',
                'location',
            ]
        })
    ]

@admin.register(EventsConfig)
class EventsConfigAdmin(SingletonModelAdmin):
    pass
