from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class ArticlesApp(CMSApp):
    name = _("Articles & Publications App")
    urls = ["articles.urls"]
    app_name = "articles"

apphook_pool.register(ArticlesApp)
