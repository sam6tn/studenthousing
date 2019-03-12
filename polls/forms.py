from django import forms
from .models import Post

class SuggestForm(forms.ModelForm):
    search = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 1}))

    class Meta:
        model = Post
        fields = ('search',)