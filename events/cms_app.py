from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class EventsApp(CMSApp):
    name = _("Events App")
    urls = ["events.urls"]
    app_name = "events"

apphook_pool.register(EventsApp)
