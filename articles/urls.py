from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView
import pagination
from .views import index, index_by_tag, detail

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    # redirect the url for the first page to just the index
    url(r'^page/1/$', RedirectView.as_view(pattern_name='articles:index'), name='first_page_redirect'),
    url(r'^page/(?P<page_number>\d+)/$', index, name='index_paged'),

    # filtered by tag
    url(r'^tag/(?P<tag>[-\w]+)/$', index_by_tag, name='index_by_tag'),
    # redirect the url for the first page to just the index
    url(r'^tag/(?P<tag>[-\w]+)/page/1/$', RedirectView.as_view(pattern_name='articles:index_by_tag'), name='first_page_tag_redirect'),
    url(r'^tag/(?P<tag>[-\w]+)/page/(?P<page_number>\d+)/$', index_by_tag, name='index_by_tag_paged'),

    url(r'^(?P<slug>[-\w]+)/$', detail, name='detail'),
)

