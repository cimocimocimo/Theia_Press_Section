from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class VideosApp(CMSApp):
    name = _("Videos App")
    urls = ["videos.urls"]
    app_name = "videos"

apphook_pool.register(VideosApp)
