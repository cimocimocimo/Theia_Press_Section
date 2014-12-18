from django.conf.urls import patterns, url

from press_items import views

view_args = {'item_filter': 'events'}

urlpatterns = patterns('',
    url(r'^$', views.index, kwargs=view_args, name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, kwargs=view_args, name='detail'),
)

# **TODO** add additional url files for the extra app hooks for articles & pubs, and events
