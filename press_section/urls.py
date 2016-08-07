from cms.sitemaps import CMSSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles import views as staticfiles_views
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', sitemap,
        {
            'sitemaps': {
                'cmspages': CMSSitemap
            }
        }
    ),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', staticfiles_views.static.serve,  # NOQA
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }
        ),
    ] + staticfiles_urlpatterns() + urlpatterns  # NOQA
