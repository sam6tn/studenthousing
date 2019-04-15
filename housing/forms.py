from django import forms
from .models import Post, Review, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import itertools

class SearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}), required=False, label="Search Locations, Addresses, or Info")
    CHOICES = (
        ('rating', 'Recommended'),
        ('available', 'Availability'),
        ('price', 'Price'),
    )
    filter = forms.ChoiceField(choices=CHOICES, widget=forms.Select, required=False)
    class Meta:
        model = Post
        fields = ('search', 'filter')

class RoommateForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}))
    class Meta:
        model = User
        fields = ('search',)


class ReviewForm(forms.ModelForm):

    CHOICES = (('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',), ('5', '5',))
    rating = forms.ChoiceField(choices=CHOICES,widget = forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    # rating = forms.IntegerField(min_value=1,max_value=5)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 3}))
    class Meta:
        model = Review
        fields = ('review_text', 'rating')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )

class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 4}))
    class Meta:
        model = Profile
        fields = (
            'year',
            'bio',
            'phone',
            'image',
            'need_roommate',
        )
