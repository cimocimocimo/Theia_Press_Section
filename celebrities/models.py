from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from ordered_model.models import OrderedModel

class Celebrity(OrderedModel):

    class Meta(OrderedModel.Meta):
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'

    name = models.CharField(max_length=256)
    byline = models.CharField(max_length=128, blank=True, null=True)
    main_image = FilerImageField()
    content = PlaceholderField('celebrity_content')

    # **TODO** celebrity tags?

    slug_max_length = 256
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.name


class Dress(OrderedModel):

    class Meta(OrderedModel.Meta):
        verbose_name = 'Dress'
        verbose_name_plural = 'Dresses'

    title = models.CharField(max_length=256)
    # event dress worn at?
    celebrity = models.ForeignKey(Celebrity)
    main_image = FilerImageField()
    order_with_respect_to = 'celebrity'
    content = PlaceholderField('celebrity_content')
    # tags?
    # link to dress product page

    slug_max_length = 256
    slug = models.SlugField(max_length=slug_max_length, unique=True)

    def __unicode__(self):
        return self.title
