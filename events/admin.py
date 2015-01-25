from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from events.models import Event
from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.
@admin.register(Event)
class EventAdmin(AdminImageMixin, PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
