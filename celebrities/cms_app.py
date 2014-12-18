from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class CelebritiesApp(CMSApp):
    name = _("Celebrities App")        # give your app a name, this is required
    urls = ["celebrities.urls"]       # link your app to url configuration(s)
    app_name = "celebrities"          # this is the application namespace

apphook_pool.register(CelebritiesApp)
