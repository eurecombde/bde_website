from .views import BlogPostFeed, ScreeningsFeed

from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('bde_eurecom.apps.movieclub.views',
    url(r'^$', 'blog', name='blog'),
    url(r'^blog\.atom$', BlogPostFeed(), name='blog_feed'),
    url(r'^blog/(?P<post_slug>.+)$', 'post_details', name='post_details'),
    url(r'^program/$', 'program', name='program'),
    url(r'^program\.atom$', ScreeningsFeed(), name='screenings_feed'),
    url(r'^program/(?P<screening_id>\d+)$', 'screening_details', name='screening_details'),
)
