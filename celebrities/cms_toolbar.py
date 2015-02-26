from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

@toolbar_pool.register
class CelebritiesToolbar(CMSToolbar):

    def populate(self):
        menu_items_data = [
            ('admin:celebrities_celebrity_changelist', 'Celebrities overview'),
            ('admin:celebrities_celebrity_add', 'Add Celebrity'),
            'break',
            ('admin:celebrities_dress_changelist', 'Dresses overview'),
            ('admin:celebrities_dress_add', 'Add Dress'),
        ]
        
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('celebrities-app', _('Celebrities'))
            for item in menu_items_data:
                if item == 'break':
                    menu.add_break()
                else:
                    menu.add_sideframe_item(
                        _(item[1]),
                        url=reverse(item[0])
                    )

    def post_template_populate(self):
        pass

    def request_hook(self):
        pass
