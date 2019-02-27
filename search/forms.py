from django import forms
from .models import Search

class SuggestForm(forms.ModelForm):
    search = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 1}))

    class Meta:
        model = Search
        fields = ('search',)