from . import tz_france
from .models import BlogPost, Screening

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import render_to_response
from django.http import Http404
from datetime import datetime

def home(request):
    posts = BlogPost.objects.filter(time_published__lte=tz_france.localize(datetime.now()))
    context = {
        'posts': posts,
    }
    return render_to_response('movieclub/home.djhtml', context)


class BlogPostFeed(Feed):
    feed_type = Atom1Feed
    title = 'Eurecom Movie Club - Blog'
    subtitle = 'Blog posts from the Eurecom movie club'
    link = '/movieclub/'


    def items(self):
        return BlogPost.objects.all()[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text


def program(request):
    screenings = Screening.objects.all()
    context = {
        'screenings': screenings,
    }
    return render_to_response('movieclub/program.djhtml', context)


def post_details(request, post_slug):
    try:
        post = BlogPost.objects.filter(slug=post_slug).get()
    except BlogPost.DoesNotExist:
        raise Http404
    context = {
        'post': post,
    }
    return render_to_response('movieclub/post_details.djhtml', context)
