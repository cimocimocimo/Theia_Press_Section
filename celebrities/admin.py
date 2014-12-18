from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from celebrities.models import Celebrity, Dress

class DressInline(admin.StackedInline):
    model = Dress
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Celebrity)
class CelebrityAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        DressInline,
    ]    

@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
