from __future__ import unicode_literals

from . import tz_france
from .models import BlogPost, Screening

from django.core.files import File
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client, TestCase
from datetime import datetime, timedelta
import tempfile

class MovieClubBlogTest(TestCase):

    def setUp(self):
        self.client = Client()
        testuser = User.objects.create(username='testuser')
        BlogPost.objects.create(title='Test blog post', markdown='This is **markdown**.', author=testuser)
        BlogPost.objects.create(title='Future post', markdown='Not visible', author=testuser,
            time_published=tz_france.localize(datetime.now() + timedelta(minutes=5)))


    def test_front_page(self):
        response = self.client.get('/movieclub/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('This is <strong>markdown</strong>' in response.content.decode('utf-8'))
        self.assertFalse('Not visible' in response.content.decode('utf-8'))


    def test_post_details(self):
        post_url = reverse('movieclub:post_details', kwargs={'post_slug': 'test-blog-post'})
        response = self.client.get(post_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('This is <strong>markdown</strong>' in response.content.decode('utf-8'))


class MovieClubProgramTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.testimage = tempfile.NamedTemporaryFile(delete=False)
        Screening.objects.create(movie_name='Test Movie 1', description_md='**super awesome**.',
            time=tz_france.localize(datetime.now()), image=File(self.testimage))
        Screening.objects.create(movie_name="It's a Wonderful Life", description_md='also *pretty cool*.',
            time=tz_france.localize(datetime.now()), image=File(self.testimage))


    def test_program(self):
        response = self.client.get('/movieclub/program/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<strong>super awesome</strong>' in response.content.decode('utf-8'))


    def test_screening_details(self):
        response = self.client.get('/movieclub/program/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<strong>super awesome</strong>' in response.content.decode('utf-8'))
