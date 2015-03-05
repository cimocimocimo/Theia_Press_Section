from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import CelebritiesPluginModel, Celebrity

class CelebritiesPlugin(CMSPluginBase):
    model = CelebritiesPluginModel
    name = _("Celebrities Plugin")
    render_template = "celebrities/celebrities_plugin.tmpl.html"

    def render(self, context, instance, placeholder):
        items = Celebrity.objects.all()[:instance.number_to_show]
        context.update({'instance':instance,
                        'celebrities':items})
        return context

plugin_pool.register_plugin(CelebritiesPlugin)


