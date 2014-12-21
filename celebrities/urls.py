from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView
from .views import index, celeb_detail, dress_detail

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    # redirect the url for the first page to just the index
    url(r'^page/1/$', RedirectView.as_view(pattern_name='celebrities:index'), name='first_page_redirect'),
    url(r'^page/(?P<page_number>\d+)/$', index, name='index_paged'),
    url(r'^(?P<slug>[-\w]+)/$', celeb_detail, name='celeb_detail'),
    url(r'^(?P<celeb_slug>[-\w]+)/(?P<dress_slug>[-\w]+)$', dress_detail, name='dress_detail'),
)

