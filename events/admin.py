from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Event, EventsConfig, EventLocationHours
from sorl.thumbnail.admin import AdminImageMixin
from solo.admin import SingletonModelAdmin

# Register your models here.
class EventLocationHoursAdmin(admin.TabularInline):
    model = EventLocationHours
    extra = 7

    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra

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
                'excerpt',
                'content',
                'main_image',
            ]
        }),
        ('Date & Time', {
            'fields': [
                'all_day',
                'from_datetime',
                'to_datetime',
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
        }),
        ('Store Hours', {
            'fields': [
                'by_appointment_only',
            ]
        })
    ]
    inlines = [EventLocationHoursAdmin,]

@admin.register(EventsConfig)
class EventsConfigAdmin(SingletonModelAdmin):
    pass

