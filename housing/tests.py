import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from housing.models import Post, Profile, Review
from housing.forms import SearchForm, RoommateForm, ReviewForm, EditProfileForm, EditUserForm



def create_search(info):
    form = SearchForm()
    form.search(info)
    return form


class PostTests(TestCase):
    def create_post(self, name, info, rating):
        return Post.objects.create(name=name, info=info, rating=rating)

    def test_new_post(self):
        p = self.create_post("", "",1)
        self.assertTrue(isinstance(p, Post))


class ReviewTests(TestCase):
    def create_post(self, name, info, rating):
        return Post.objects.create(name=name, info=info, rating=rating)

    def create_review(self, post, review_text, rating):
        return Review.objects.create(post=post, review_text=review_text, rating=rating)

    def test_new_review(self):
        p = self.create_post("", "",4)
        r = self.create_review(p, 'nice place', 5)
        self.assertTrue(isinstance(r, Review))


class ViewTests(TestCase):
    def create_post(self, name, info, rating):
        return Post.objects.create(name=name, info=info, rating=rating)

    def test_search_results_found(self):
        p = self.create_post(name="", info="", rating=1)
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


class SearchFormTests(TestCase):
    def test_SearchForm_valid_empty(self):
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


class RoommateFormTests(TestCase):
    def test_RoommateForm_valid_empty(self):
        form = SearchForm(data={'search': "", 'year': [], 'gender': []})
        self.assertTrue(form.is_valid())

    def test_RoommateForm_valid(self):
        form = RoommateForm(data={'search': "clean", 'year': ["1"], 'gender': ['t']})
        self.assertTrue(form.is_valid())

    def test_RoommateForm_invalid_year(self):
        form = RoommateForm(data={'search': 'h', 'year': ['6'], 'gender': ['t']})
        self.assertFalse(form.is_valid())

    def test_RoommateForm_invalid_gender(self):
        form = RoommateForm(data={'search':'h', 'year': ['2','5'], 'gender': ['pnts']})
        self.assertFalse(form.is_valid())


class ReviewFormTests(TestCase):
    def test_ReviewForm_valid(self):
        form = ReviewForm(data={'rating': "1", 'review_text': "not good"})
        self.assertTrue(form.is_valid())

    def test_ReviewForm_invalid_no_review_text(self):
        form = ReviewForm(data={'rating': "1", 'review_text': ""})
        self.assertFalse(form.is_valid())

    def test_ReviewForm_invalid_rating(self):
        form = ReviewForm(data={'rating': "10", 'review_text': "nice place"})
        self.assertFalse(form.is_valid())

    def test_ReviewForm_invalid_no_rating(self):
        form = ReviewForm(data={'rating': "", 'review_text': "nice place"})
        self.assertFalse(form.is_valid())


class EditProfileFormTests(TestCase):
    def test_EditProfileForm_valid(self):
        form = EditProfileForm(data={'phone':'1234567890', 'year':'u', 'gender':'u', 'bio':'', 'image':'', 'need_roommate':True})
        self.assertTrue(form.is_valid())

    def test_EditProfileForm_invalid_empty(self):
        form = EditProfileForm(data={'phone':'', 'year':'', 'gender':'', 'bio':'', 'image':'', 'need_roommate':''})
        self.assertFalse(form.is_valid())

    def test_EditProfileForm_invalid_phone(self):
        form = EditProfileForm(data={'phone':'123456789000', 'year':'u', 'gender':'u', 'bio':'', 'image':'', 'need_roommate':True})
        self.assertFalse(form.is_valid())

    def test_EditProfileForm_invalid_phone2(self):
        form = EditProfileForm(data={'phone':'12345', 'year':'u', 'gender':'u', 'bio':'', 'image':'', 'need_roommate':True})
        self.assertFalse(form.is_valid())

    def test_EditProfileForm_invalid_gender(self):
        form = EditProfileForm(data={'phone':'1234567890', 'year':'u', 'gender':['m','w'], 'bio':'', 'image':'', 'need_roommate':True})
        self.assertFalse(form.is_valid())

    def test_EditProfileForm_invalid_year(self):
        form = EditProfileForm(data={'phone':'1234567890', 'year':'6', 'gender':'m', 'bio':'', 'image':'', 'need_roommate':True})
        self.assertFalse(form.is_valid())


class EditUserFormTests(TestCase):
    def test_EditUserForm_valid(self):
        form = EditUserForm(data={'email':'foo@virginia.edu', 'first_name':'jon', 'last_name':'snow'})
        self.assertTrue(form.is_valid())

    def test_EditUserForm_invalid_empty(self):
        form = EditUserForm(data={'email': '', 'first_name': '', 'last_name': ''})
        self.assertTrue(form.is_valid())

    def test_EditUserForm_invalid_email(self):
        form = EditUserForm(data={'email':'foo@gmail', 'first_name':'jon', 'last_name':'snow'})
        self.assertFalse(form.is_valid())

    def test_EditUserForm_invalid_email2(self):
        form = EditUserForm(data={'email':'@gmail.com', 'first_name':'jon', 'last_name':'snow'})
        self.assertFalse(form.is_valid())