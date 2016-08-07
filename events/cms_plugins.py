from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import EventsPluginModel, Event
import datetime

class EventsPlugin(CMSPluginBase):
    model = EventsPluginModel
    name = _("Events Plugin")
    render_template = "events/events_plugin.tmpl.html"

    def render(self, context, instance, placeholder):
        today_less_one_day = datetime.date.today() - datetime.timedelta(days=1)
        query_set = Event.objects.filter(to_datetime__gt=today_less_one_day).order_by('to_datetime')

        if query_set.count() > 0:
            item = query_set[:1][0]
        else:
            item = False

        context.update({'instance':instance,
                        'event':item})
        return context

plugin_pool.register_plugin(EventsPlugin)


