from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
import datetime

class Article(models.Model):

    slug_max_length = 256

    title = models.TextField(
        max_length=256)
    slug = models.SlugField(
        max_length=64,
        unique=True)
    organization_name = models.TextField(
        max_length=256,
        blank=True,
        default='')
    url = models.URLField(
        max_length=512,
        blank=True,
        default='')
    original_publication_date = models.DateField(
        blank=True,
        null=True)
    published_date = models.DateField(
        default=datetime.date.today())
    content = PlaceholderField('press_item_content')

    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title




