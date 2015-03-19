import os
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import GalleryPluginModel, Gallery, PressImage, ImageFile

class GalleryPlugin(CMSPluginBase):
    model = GalleryPluginModel
    name = _("Gallery Plugin")
    render_template = "gallery/gallery.tmpl.html"

    def render(self, context, instance, placeholder):

        # get the images for the selected gallery
        images = PressImage.objects.filter(gallery=instance.gallery)

        for img in images:
            # get the files attached to this image
            files = ImageFile.objects.filter(press_image=img)
            if files.exists():
                img.files = files

            # set the format for the thumbnail
            file_extension = os.path.splitext(img.image.name)[1]
            if file_extension == '.png':
                img.thumb_format = 'PNG'
            else:
                img.thumb_format = 'JPEG'
        context.update({'gallery':instance.gallery,
                        'images':images})
        return context

plugin_pool.register_plugin(GalleryPlugin)
