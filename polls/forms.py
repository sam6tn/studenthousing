from django import forms
from .models import Post

class SuggestForm(forms.ModelForm):
    search = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 1}))

    class Meta:
        model = Post
        fields = ('search',)

# class LoginForm(forms.ModelForm):
#     email = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 1}))
#     password = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 1}))