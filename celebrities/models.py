from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from ordered_model.models import OrderedModel
from sorl.thumbnail import ImageField

class Celebrity(OrderedModel):

    class Meta(OrderedModel.Meta):
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'

    name = models.CharField(max_length=255)
    byline = models.CharField(max_length=128, blank=True, null=True)
    main_image = ImageField(null=True, blank=True)
    content = PlaceholderField('celebrity_content')

    # **TODO** celebrity tags?

    slug_max_length = 255
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.name


class Dress(OrderedModel):

    class Meta(OrderedModel.Meta):
        verbose_name = 'Dress'
        verbose_name_plural = 'Dresses'

    title = models.CharField(max_length=255)
    # event dress worn at?
    celebrity = models.ForeignKey(Celebrity)
    main_image = ImageField(null=True, blank=True)
    order_with_respect_to = 'celebrity'
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
    
