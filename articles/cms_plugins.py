from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import LatestArticlesPluginModel, Article

class LatestArticlesPlugin(CMSPluginBase):
    model = LatestArticlesPluginModel
    name = _("Latest Articles Plugin")
    render_template = "articles/latest_articles_plugin.tmpl.html"

    def render(self, context, instance, placeholder):
        items = Article.objects.order_by('original_publication_date')[:instance.number_to_show]
        context.update({'instance':instance,
                        'articles':items})
        return context

plugin_pool.register_plugin(LatestArticlesPlugin)
