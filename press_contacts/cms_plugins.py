from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import PressContactPluginModel

class PressContactPlugin(CMSPluginBase):
    model = PressContactPluginModel
    name = _("Press Contact Plugin")
    render_template = "press_contacts/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(PressContactPlugin)
