from . import tz_france
from .models import BlogPost, Screening

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import render_to_response, get_object_or_404
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
        'active': 'program',
    }
    return render_to_response('movieclub/program.djhtml', context)


def post_details(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
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
    }
    return render_to_response('movieclub/screening_details.djhtml', context)
