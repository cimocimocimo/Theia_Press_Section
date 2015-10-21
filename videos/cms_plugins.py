from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import VideosPluginModel, Video

class VideosPlugin(CMSPluginBase):
    model = VideosPluginModel
    name = _("Videos Plugin")
    render_template = "videos/videos_plugin.tmpl.html"

    def render(self, context, instance, placeholder):
        item = Video.objects.all()[:1][0]
        context.update({'instance':instance,
                        'video':item})
        return context

plugin_pool.register_plugin(VideosPlugin)


