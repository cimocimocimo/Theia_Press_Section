from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from sorl.thumbnail import ImageField

import datetime

class Event(models.Model):

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    slug_max_length = 255

    title = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=64,
        unique=True)
    event_date = models.DateField(
        default=datetime.date.today)
    published_date = models.DateTimeField(
        default=datetime.datetime.now)
    excerpt = models.TextField(null=True, blank=True)
    content = PlaceholderField('event_content')
    video_still = ImageField(null=True, blank=True)

    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title




