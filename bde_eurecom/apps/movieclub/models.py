from . import tz_france

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_delete
from django.utils.text import slugify
from os import path
from markdown import markdown
from datetime import datetime

_MARKDOWN_HELP_TEXT = ("Markdown supported. If you're new to markdown you can play around with "
    "<a href=\"http://dillinger.io/\" target=\"_blank\">dillinger.io </a> to learn the syntax")


def upload_blog_post_image(instance, filename):
    original_extension = path.splitext(filename)[1]
    filename = '%s-%s%s' % (instance.time_published.date(), instance.slug, original_extension)
    return path.join('movieclub', filename)


class BlogPost(models.Model):
    image = models.ImageField(upload_to=upload_blog_post_image, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, unique=True)
    time_published = models.DateTimeField(help_text=("Set into the future if you don't want the "
        "post to be visible yet. Leave blank to default to now."),
        blank=True)
    time_added = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='movieclub_blog_posts')
    markdown = models.TextField('text', help_text=_MARKDOWN_HELP_TEXT)
    text = models.TextField()


    class Meta:
        ordering = ['-time_published']


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.time_published:
            self.time_published = tz_france.localize(datetime.now())
        self.slug = slugify(self.title)
        self.text = markdown(self.markdown, ['smarty'])
        return super(BlogPost, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('movieclub:post_details', kwargs={'post_slug': self.slug})


def upload_screening_image(instance, orig_filename):
    filename = '%s-%s%s' % (instance.time.date(), instance.slug, path.splitext(orig_filename)[1])
    return path.join('movieclub', filename)


class Screening(models.Model):
    movie_name = models.CharField(max_length=100)
    time = models.DateTimeField()
    description = models.TextField(blank=True)
    description_md = models.TextField('description', help_text=_MARKDOWN_HELP_TEXT)
    movie_link = models.URLField(help_text=("Search for the movie on "
        "<a href=\"http://www.themoviedb.com\" target=\"_blank\">TheMovieDB</a> and copy the link "
        "from there"))
    image = models.ImageField(upload_to=upload_screening_image, help_text=("TheMovieDB has some "
        "great backdrops, browse through them and find one you like, download it to your machine "
        "by right-clicking and click 'Save image as', and upload that picture here. (don't take the "
        "full-size ones, they're way too big)"))
    added_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-time']

    def __str__(self):
        return '%s: %s' % (self.time.date(), self.movie_name)


    def save(self, *args, **kwargs):
        self.description = markdown(self.description_md, ['smarty'])
        return super(Screening, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('movieclub:screening_details', kwargs={'screening_id': self.id})


    @property
    def slug(self):
        return slugify(self.movie_name)


@receiver(pre_delete, sender=Screening)
def delete_movie_image(sender, instance, **kwargs):
    print 'In pre_delete!'
    print instance
    instance.image.delete()
