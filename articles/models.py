from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

import datetime

class Article(models.Model):

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    slug_max_length = 255

    title = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=64,
        unique=True)
    organization_name = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    url = models.URLField(
        max_length=512,
        blank=True,
        null=True)
    original_publication_date = models.DateField(
        default=datetime.date.today)
    published_date = models.DateTimeField(
        default=datetime.datetime.now)
    content = PlaceholderField('press_item_content')
    excerpt = models.TextField(blank=True, null=True)
    # screenshot = FilerImageField(null=True, blank=True)

    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title




