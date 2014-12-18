from django.conf.urls import patterns, url

from celebrities import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.celeb_detail, name='celeb_detail'),
    url(r'^(?P<celeb_slug>[-\w]+)/(?P<dress_slug>[-\w]+)$', views.dress_detail, name='dress_detail'),
)

