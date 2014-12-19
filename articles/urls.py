from django.conf.urls import patterns, url

from press_items import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='detail'),
)

