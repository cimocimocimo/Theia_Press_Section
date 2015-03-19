from django.db import models
from cms.models import CMSPlugin
from ordered_model.models import OrderedModel
from sorl.thumbnail import ImageField
from django.utils.encoding import python_2_unicode_compatible

# Gallery
@python_2_unicode_compatible
class Gallery(models.Model):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    title = models.CharField(max_length=256)

# Image
@python_2_unicode_compatible
class PressImage(OrderedModel):

    def __str__(self):
        return self.image.name

    class Meta(OrderedModel.Meta):
        verbose_name = 'Press Image'
        verbose_name_plural = 'Press Images'

    image = ImageField()
    caption = models.CharField(null=True, blank=True, max_length=255)
    gallery = models.ForeignKey(Gallery)

# file
@python_2_unicode_compatible
class ImageFile(models.Model):
    
    def __str__(self):
        return self.link_text

    class Meta:
        verbose_name = 'Image File'
        verbose_name_plural = 'Image Files'

    file = models.FileField()
    link_text = models.CharField(max_length=128)
    press_image = models.ForeignKey(PressImage)

class GalleryPluginModel(CMSPlugin):
    gallery = models.ForeignKey('gallery.Gallery', related_name='plugins')
