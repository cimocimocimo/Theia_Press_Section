from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from adminsortable.models import SortableMixin
from sorl.thumbnail import ImageField

class Celebrity(SortableMixin):

    class Meta:
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'
        ordering = ['order']

    name = models.CharField(max_length=255)
    byline = models.CharField(max_length=128, blank=True, null=True)
    main_image = ImageField(null=True, blank=True)
    content = PlaceholderField('celebrity_content')

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    order_field_name = 'order'

    # **TODO** celebrity tags?

    slug_max_length = 255
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.name


class Dress(models.Model):

    class Meta:
        verbose_name = 'Dress'
        verbose_name_plural = 'Dresses'

    title = models.CharField(max_length=255)
    # event dress worn at?
    celebrity = models.ForeignKey(Celebrity)
    main_image = ImageField(null=True, blank=True)
    content = PlaceholderField('celebrity_content')

    # tags?
    # link to dress product page

    slug_max_length = 255
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.title

class CelebritiesPluginModel(CMSPlugin):
    number_to_show = models.PositiveSmallIntegerField(default=4)
    title = models.CharField(max_length=255,
                             default="Celebrities")
