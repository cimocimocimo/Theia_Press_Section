from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import EventsPluginModel, Event

class EventsPlugin(CMSPluginBase):
    model = EventsPluginModel
    name = _("Events Plugin")
    render_template = "events/events_plugin.tmpl.html"

    def render(self, context, instance, placeholder):
        item = Event.objects.all()[:1][0]
        context.update({'instance':instance,
                        'event':item})
        return context

plugin_pool.register_plugin(EventsPlugin)


