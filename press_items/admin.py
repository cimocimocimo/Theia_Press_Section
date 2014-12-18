from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from press_items.models import PressItem, PressItemType

# Register your models here.
@admin.register(PressItem)
class PressItemAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PressItemType)
class PressItemTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

