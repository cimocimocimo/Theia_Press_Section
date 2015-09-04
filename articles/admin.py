from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from articles.models import Article
from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.
@admin.register(Article)
class ArticleAdmin(AdminImageMixin, PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': [
                'title',
                'slug',
                ('organization_name',
                 'url',),
                ('original_publication_date',
                 'original_publication_date_label',),
                'excerpt',
                'lead_content',
                ('screenshot',
                 'screenshot_2',),
                'tags',]}),)
