from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
import datetime

class Event(models.Model):

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    slug_max_length = 256

    title = models.CharField(
        max_length=256)
    slug = models.SlugField(
        max_length=64,
        unique=True)
    event_date = models.DateField(
        default=datetime.date.today)
    published_date = models.DateTimeField(
        default=datetime.datetime.now)
    content = PlaceholderField('event_content')
    video_still = FilerImageField(null=True, blank=True)

    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title




