import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Post
from polls.forms import SearchForm, ReviewForm


def create_post(name, info, rating):
    return Post.objects.create(name=name, info=info, rating=rating)

def create_search(info):
    form = SearchForm()
    form.search(info)
    return form


class PostTests(TestCase):
    def test_new_post(self):
        p = create_post(name="", info="", rating=1)
        self.assertEqual(p.rating, 1)

    #def test_search_posted(self):
    #    p = create_post(name="", info="", rating=1)
    #    url = reverse('housing:housingsearch')
    #    response = self.client.get(url)
    #    self.assertContains(response, p.name)

class ViewTests(TestCase):
    def test_search_results_found(self):
        p = create_post(name="", info="", rating=1)
        url = reverse('housing:housingsearch')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_roommate_results_found(self):
        url = reverse('housing:roommates')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_login_response(self):
        url = reverse('social:begin', kwargs={'backend': 'google-oauth2'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_logout_response(self):
        url = reverse('housing:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_wrong_login_response(self):
        url = reverse('social:begin', kwargs={'backend': 'blabla'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class FormTests(TestCase):
    def test_SearchForm_valid_nothing(self):
        form = SearchForm(data={'search': "", 'filter': ""})
        self.assertTrue(form.is_valid())

    def test_SearchForm_valid_only_search(self):
        form = SearchForm(data={'search': "charlottesville", 'filter': ""})
        self.assertTrue(form.is_valid())

    def test_SearchForm_valid_only_filter(self):
        form = SearchForm(data={'search': "", 'filter': "rating"})
        self.assertTrue(form.is_valid())

    def test_SearchForm_invalid(self):
        form = SearchForm(data={'search': "", 'filter': "name"})
        self.assertFalse(form.is_valid())

    def test_ReviewForm_valid(self):
        form = ReviewForm(data={'rating': "1", 'review_text': "not good"})
        self.assertTrue(form.is_valid())

    def test_ReviewForm_invalid(self):
        form = ReviewForm(data={'rating': "1", 'review_text': ""})
        self.assertFalse(form.is_valid())
"""
    def test_filter(self):
        p1 = create_post(name="", info="", rating=1)
        p2 = create_post(name="", info="", rating=5)
        url = reverse('housing:housingsearch')
        form = SearchForm(data={'search': "", 'filter': "rating"})
        response = self.client.get(url)
"""

"class PostSuggestView(TestCase):"