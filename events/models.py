from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from sorl.thumbnail import ImageField
from location_field.models.plain import PlainLocationField
from press_contacts.models import PressContact
from solo.models import SingletonModel
from tinymce.models import HTMLField
from django.utils import timezone

class EventsConfig(SingletonModel):
    contact = models.ForeignKey(
        'press_contacts.PressContact',
        null=True,
        blank=True)

    def __unicode__(self):
        return 'Events Configuration'

    class Meta:
        verbose_name = "Events Configuration"

class Event(models.Model):

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    title = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=64,
        unique=True)
    all_day = models.BooleanField(
        default=True)
    from_datetime = models.DateTimeField(
        default=timezone.now)
    to_datetime = models.DateTimeField(
        default=timezone.now)

    by_appointment_only = models.BooleanField(
        default=False)
    appointment_only_info = models.TextField(
        null=True,
        blank=True)

    published_date = models.DateTimeField(
        default=timezone.now)
    excerpt = models.TextField(null=True, blank=True)
    content = HTMLField(
        null=True,
        blank=True)
    main_image = ImageField(null=True, blank=True)
    location_name = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    address = models.TextField(
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

    @property
    def is_single_day(self):
        return (self.from_datetime.date() == self.to_datetime.date())

    @property
    def is_within_same_month(self):
        if self.from_datetime.year == self.to_datetime.year:
            return self.from_datetime.month == self.to_datetime.month
        return False

    @property
    def has_location_hours(self):
        hours = EventLocationHours.objects.filter(event__pk=self.id)
        return len(hours) > 0

class EventsPluginModel(CMSPlugin):
    title = models.CharField(
        max_length=255,
        default="Events")

class EventLocationHours(models.Model):
    class Meta:
        unique_together = (('event', 'weekday'),)

    WEEKDAYS = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]

    event = models.ForeignKey(
        Event
    )
    weekday = models.IntegerField(
        choices=WEEKDAYS,
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
