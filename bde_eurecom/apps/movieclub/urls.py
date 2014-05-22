from .views import BlogPostFeed

from django.conf.urls import patterns, url
from django.contrib import admin
#from bde_eurecom.apps.housing.models import House

admin.autodiscover()

urlpatterns = patterns('bde_eurecom.apps.movieclub.views',
    url(r'^$', 'home', name='home'),
    url(r'^blog\.atom$', BlogPostFeed(), name='blog_feed'),
    url(r'^program/$', 'program', name='program'),
    url(r'^blog/(?P<post_slug>.+)$', 'post_details', name='post_details'),
)
