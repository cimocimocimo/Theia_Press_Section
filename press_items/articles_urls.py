from django.conf.urls import patterns, url

from press_items import views

view_args = {'item_filter': 'articles'}

urlpatterns = patterns('',
    url(r'^$', views.index, kwargs=view_args, name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='detail'),
)
