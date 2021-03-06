from django.conf.urls import url, include
from django.views.generic import RedirectView
import pagination
from .views import index, detail

urlpatterns = [
    url(r'^$', index, name='index'),
    # redirect the url for the first page to just the index
    url(r'^page/1/$', RedirectView.as_view(pattern_name='events:index'), name='first_page_redirect'),
    url(r'^page/(?P<page_number>\d+)/$', index, name='index_paged'),
    url(r'^(?P<slug>[-\w]+)/$', detail, name='detail'),
]
