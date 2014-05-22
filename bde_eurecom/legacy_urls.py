"""
    Legacy URLs that have been moved, that we need to redirect.

    For now all of them are from the movieclub site, which was previusly hosted at the root directory.

"""

from django.conf.urls import patterns, url
from django.shortcuts import redirect


def blog_posts_redirect(requests, post_slug):
    if post_slug[-1] == '/':
        post_slug = post_slug[:-1]
    return redirect('movieclub:post_details', post_slug=post_slug, permanent=True)


legacy_patterns = patterns('',
    url(r'^blog/(?P<post_slug>.*)$', blog_posts_redirect),
    url(r'^program/$', lambda r: redirect('movieclub:program', permanent=True)),
)
