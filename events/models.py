from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from sorl.thumbnail import ImageField
from location_field.models.plain import PlainLocationField
from press_contacts.models import PressContact

import datetime

class Event(models.Model):

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    title = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=64,
        unique=True)
    event_date_from = models.DateTimeField(
        default=datetime.datetime.now)
    event_date_to = models.DateTimeField(
        default=datetime.datetime.now)
    published_date = models.DateTimeField(
        default=datetime.datetime.now)
    excerpt = models.TextField(null=True, blank=True)
    content = PlaceholderField('event_content')
    main_image = ImageField(null=True, blank=True)
    location_name = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    address = models.CharField(
        max_length=255,
        default='New York, NY',
        help_text='Used to search Google for the location.')
    location = PlainLocationField(
        based_fields=[address],
        zoom=7,
        null=True,
        blank=True)
    event_contact = models.ForeignKey(
        'press_contacts.PressContact',
        null=True,
        blank=True)
    extra_contact_information = models.TextField(null=True, blank=True)
    # **TODO** Add django-taggit

    def __unicode__(self):
        return self.title


class EventsPluginModel(CMSPlugin):
    title = models.CharField(max_length=255,
                             default="Events")
