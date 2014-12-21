from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from events.models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
