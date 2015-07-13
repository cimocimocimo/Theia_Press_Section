from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

@toolbar_pool.register
class EventsToolbar(CMSToolbar):

    def populate(self):
        menu_items_data = [
            ('admin:events_event_changelist', 'Events overview'),
            ('admin:events_event_add', 'Add event')
        ]

        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('events-app', _('Events'))
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
