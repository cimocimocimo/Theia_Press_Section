from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from ordered_model.admin import OrderedModelAdmin

from celebrities.models import Celebrity, Dress

class DressInline(admin.TabularInline):
    model = Dress
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'move_up_down_links')

@admin.register(Celebrity)
class CelebrityAdmin(PlaceholderAdminMixin, OrderedModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'move_up_down_links')
    inlines = [
        DressInline,
    ]    

@admin.register(Dress)
class DressAdmin(OrderedModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
