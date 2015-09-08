from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from adminsortable.admin import SortableAdmin
from sorl.thumbnail.admin import AdminImageMixin

from celebrities.models import Celebrity, Dress

class DressInline(admin.TabularInline):
    model = Dress
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)

@admin.register(Celebrity)
class CelebrityAdmin(AdminImageMixin, PlaceholderAdminMixin, SortableAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    inlines = [
        DressInline,
    ]    

@admin.register(Dress)
class DressAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
