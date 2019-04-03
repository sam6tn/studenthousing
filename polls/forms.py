from django import forms
from .models import Post, Review, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import itertools

class SearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115,}))
    class Meta:
        model = Post
        fields = ('search',)

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1,max_value=5)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 3}))
    class Meta:
        model = Review
        fields = ('review_text','rating',)


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

"""
class SearchFilterEx(django_filters.FilterSet):
    ex = django_filters.MethodFilter()
    search_fields = ['name', 'info', 'address', ]

    def filter_ex(self, qs, value):
        if value:
            q_parts = value.split()

            # Permutation code copied from http://stackoverflow.com/a/12935562/119071

            list1 = self.search_fields
            list2 = q_parts
            perms = [zip(x, list2) for x in itertools.permutations(list1, len(list2))]

            q_totals = Q()
            for perm in perms:
                q_part = Q()
                for p in perm:
                    q_part = q_part & Q(**{p[0] + '__icontains': p[1]})
                q_totals = q_totals | q_part

            qs = qs.filter(q_totals)
        return qs

    class Meta:
        model = Post
        fields = ['ex']
"""