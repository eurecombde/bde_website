from . import tz_france
from .models import BlogPost, Screening

from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from datetime import datetime

def blog(request):
    posts = BlogPost.objects.filter(time_published__lte=tz_france.localize(datetime.now()))
    context = {
        'posts': posts,
        'active': 'blog',
    }
    return render_to_response('movieclub/home.djhtml', context)


class BlogPostFeed(Feed):
    feed_type = Atom1Feed
    title = 'Eurecom Movie Club - Blog'
    subtitle = 'Blog posts from the Eurecom movie club'

    def link(self):
        return reverse('movieclub:blog')


    def items(self):
        return BlogPost.objects.all()[:15]


    def item_title(self, item):
        return item.title


    def item_description(self, item):
        return item.text


    def item_pubdate(self, item):
        return item.time_published


class ScreeningsFeed(Feed):
    feed_type = Atom1Feed
    title = 'Eureom Movie Club - Screenings'
    subtitle = 'Movie screenings by the Eurecom movie club'

    def link(self):
        return reverse('movieclub:program')


    def items(self):
        return Screening.objects.all()[:15]


    def item_title(self, item):
        return '%s: %s' % (item.time.date().strftime('%d. %b'), item.movie_name)


    def item_description(self, item):
        return item.description


    def item_pubdate(self, item):
        return item.added_date


def program(request):
    screenings = Screening.objects.all()
    context = {
        'screenings': screenings,
        'active': 'program',
    }
    return render_to_response('movieclub/program.djhtml', context)


def post_details(request, post_slug):
    try:
        post = get_object_or_404(BlogPost, slug=post_slug)
    except Http404:
        if post_slug[-1] == '/':
            return redirect(request.path[:-1], permanent=True)
        else:
            raise
    context = {
        'post': post,
        'active': 'post_details',
        'blog_nav_text': '&larr; Back to blog',
    }
    return render_to_response('movieclub/post_details.djhtml', context)


def screening_details(request, screening_id):
    screening = get_object_or_404(Screening, id=screening_id)
    context = {
        'screening': screening,
        'active': 'screening_details',
        'program_nav_text': '&larr; Back to program',
        'image_url': request.build_absolute_uri(screening.image.url),
    }
    return render(request, 'movieclub/screening_details.djhtml', context)
