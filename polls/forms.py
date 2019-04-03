from django import forms
from .models import Post, Review, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}))
    class Meta:
        model = Post
        fields = ('search',)

class RoommateForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}))
    class Meta:
        model = User
        fields = ('search',)

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1,max_value=5)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 3}))
    class Meta:
        model = Review
        fields = ('review_text','rating',)


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
            'bio',
            'phone',
            'image',
        )

