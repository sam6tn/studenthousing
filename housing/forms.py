from django import forms
from .models import Post, Review, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import itertools

class SearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115, 'placeholder': 'Search Locations, Addresses, or Info'}), required=False)
    CHOICES = (
        ('rating', 'Recommended'),
        ('available', 'Availability'),
        ('priceup', 'Price: Low to High'),
        ('price', 'Price: High to Low'),
    )
    filter = forms.ChoiceField(choices=CHOICES, widget=forms.Select, required=False)
    class Meta:
        model = Post
        fields = ('search', 'filter')

class RoommateForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}))
    YEAR_OPTIONS = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Graduate Student'),
    )
    year = forms.MultipleChoiceField(choices=YEAR_OPTIONS, widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = User
        fields = ('search','year')


class ReviewForm(forms.ModelForm):

    CHOICES = (('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',), ('5', '5',))
    rating = forms.ChoiceField(choices=CHOICES,widget = forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    # rating = forms.IntegerField(min_value=1,max_value=5)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 3}))
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
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 4}), required=False)
    phone = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = (
            'year',
            'bio',
            'phone',
            'image',
            'need_roommate',
        )
