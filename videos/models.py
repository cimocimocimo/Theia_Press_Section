from django.db import models
from cms.models import CMSPlugin
from sorl.thumbnail import ImageField
from tinymce.models import HTMLField
from django.utils import timezone

class Video(models.Model):

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    title = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=64,
        unique=True)

    published_date = models.DateTimeField(
        default=timezone.now)
    excerpt = models.TextField(null=True, blank=True)
    content = HTMLField(
        null=True,
        blank=True)
    main_image = ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class VideosPluginModel(CMSPlugin):
    title = models.CharField(
        max_length=255,
        default="Videos")

