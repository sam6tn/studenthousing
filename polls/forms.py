from django import forms
from .models import Post, Review, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}))
    class Meta:
        model = Post
        fields = ('search',)

class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 3}))
    class Meta:
        model = Review
        fields = ('review_text',)


class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User

        exclude = ("password",)
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',


        )

        def save(self, commit=True):
            # do something with self.cleaned_data['temp_id']
            return super(EditProfileForm, self).save(commit=commit)
