from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from sorl.thumbnail import ImageField
from django.utils.encoding import python_2_unicode_compatible

import datetime

@python_2_unicode_compatible
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
    original_publication_date_label = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    published_date = models.DateTimeField(
        default=datetime.datetime.now)
    content = PlaceholderField('press_item_content')
    excerpt = models.TextField(blank=True, null=True)
    lead_content = models.TextField(blank=True, null=True)
    screenshot = ImageField(null=True, blank=True)
    screenshot_2 = ImageField(null=True, blank=True)

    # **TODO** Add django-taggit

    def __str__(self):
        return self.title


class LatestArticlesPluginModel(CMSPlugin):
    number_to_show = models.PositiveSmallIntegerField(default=4)
    title = models.CharField(max_length=255,
                             default="Latest Articles")
