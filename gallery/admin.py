from django.contrib import admin
from .models import PressImage, ImageFile, Gallery

class  ImageFileInline(admin.TabularInline):
    model = ImageFile
    extra = 1

@admin.register(PressImage)
class PressImageAdmin(admin.ModelAdmin):
    list_select_related = ('gallery',)
    inlines = [
        ImageFileInline]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = []




