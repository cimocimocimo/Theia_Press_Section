from django.contrib import admin
from .models import Video
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin

# Register your models here.
@admin.register(Video)
class VideoAdmin(AdminImageMixin, AdminVideoMixin, admin.ModelAdmin):
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
                                'video']})]



