from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

# Create your models here.

class ArticleType(models.Model):
    name = models.TextField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):

    slug_max_length = 256

    title = models.TextField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    organization_name = models.TextField(max_length=256)
    url = models.URLField(max_length=512)
    original_publication_date = models.DateField()
    published_date = models.DateField()
    content = PlaceholderField('press_item_content')
    item_type = models.ForeignKey(ArticleType)

    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title




