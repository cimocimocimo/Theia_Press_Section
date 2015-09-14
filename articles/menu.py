from menus.base import NavigationNode
from cms.menu_bases import CMSAttachMenu
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from .models import Article
from taggit.models import Tag

class ArticleTagMenu(CMSAttachMenu):
    
    name = _("Article Tag Menu")
    
    def get_link_url(self, slug):
        url = '/en/articles/{}/'.format(slug)
        return url
    
    def get_nodes(self, request):
        nodes = []
        for tag in Tag.objects.all():
            node = NavigationNode(
                tag.name,
                self.get_link_url(tag.slug),
                tag.pk + 10,
            )
            nodes.append(node)
        return nodes
    
# menu_pool.register_menu(ArticleTagMenu)
