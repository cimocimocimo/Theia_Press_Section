from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from articles.models import Article
from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.
@admin.register(Article)
class ArticleAdmin(AdminImageMixin, PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
