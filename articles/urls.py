from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from articles import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    # redirect the url for the first page to just the index
    url(r'^page/1/$', RedirectView.as_view(pattern_name='articles:index'), name='first_page_redirect'),
    url(r'^page/(?P<page_number>\d+)/$', views.index, name='index_paged'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='detail'),
)

