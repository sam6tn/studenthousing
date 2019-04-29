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
    search = forms.CharField(widget=forms.TextInput(attrs={'size': 115, 'placeholder': 'Search roommates...'}), required=False)
    YEAR_OPTIONS = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Graduate Student'),
    )
    year = forms.MultipleChoiceField(choices=YEAR_OPTIONS, widget=forms.CheckboxSelectMultiple(attrs={'class' : 'form-check'}), required=False)
    GENDER_CHOICES = (
        ('w', 'Woman'),
        ('m', 'Man'),
        ('gnc', 'Gender Non-Conforming'),
        ('t', 'Transgender'),
    )
    gender = forms.MultipleChoiceField(choices=GENDER_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class' : 'form-check'}), required=False, )

    class Meta:
        model = User
        fields = ('search', 'year', 'gender')


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
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: large', })
        }


class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 4}), required=False, help_text="Tell us about yourself! Let people know what you're looking for in a roommate.")
    phone = forms.CharField(max_length=10, min_length=10, required=False, widget=forms.TextInput(attrs={'size': 10, 'placeholder': 'Ex. 4345551234'}))

    class Meta:
        model = Profile
        fields = (
            'year',
            'gender',
            'bio',
            'phone',
            'image',
            'need_roommate',
        )
