from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from articles.models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
