import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Post


def create_post(name, info, rating):
    return Post.objects.create(name=name, info=info, rating=rating)


class PostTests(TestCase):
    def test_new_post(self):
        p = create_post(name="", info="", rating=1)
        self.assertEqual(p.rating, 1)

    def test_search_posted(self):
        p = create_post(name="", info="", rating=1)
        url = reverse('housing:list')
        response = self.client.get(url)
        self.assertContains(response, p.name)

    def test_search_results_found(self):
        p = create_post(name="", info="", rating=1)
        url = reverse('housing:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_response(self):
        url = reverse('social:begin', kwargs={'backend': 'google-oauth2'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_wrong_response(self):
        url = reverse('social:begin', kwargs={'backend': 'blabla'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


"class PostSuggestView(TestCase):"
