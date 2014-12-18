from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class PressItemsApp(CMSApp):
    name = _("Press Item App")        # give your app a name, this is required
    urls = ["press_items.urls"]       # link your app to url configuration(s)
    app_name = "press_items"          # this is the application namespace

apphook_pool.register(PressItemsApp)

class ArticlesApp(CMSApp):
    name = _("Articles & Publications App")
    urls = ["press_items.articles_urls"]
    app_name = "articles"

apphook_pool.register(ArticlesApp)

class EventsApp(CMSApp):
    name = _("Events App")
    urls = ["press_items.events_urls"]
    app_name = "events"

apphook_pool.register(EventsApp)

