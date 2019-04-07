from .forms import SearchForm, ReviewForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.utils import timezone
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import logout as user_logout
from polls.forms import EditUserForm, EditProfileForm, RoommateForm
from django.contrib.auth.models import User

from .models import Post, Review, Profile

class LoginView(TemplateView):
    template_name = 'polls/index.html'

    def post(self, request):
        return HttpResponseRedirect("/housingsearch/")

#view for housing search
class ListView(TemplateView):
    template_name = 'polls/list.html'
    model = Post
    def get(self, request):
        form = SearchForm()
        if request.user.is_authenticated:
            posts = Post.objects.all() #if no search input, displays all posts
            for post in posts:
                post_rating = 0
                count = 0
                for review in post.review_set.all():
                    post_rating += review.rating
                    count += 1
                if (count==0):
                    post.rating = 0
                else:
                    post_rating = int(round(post_rating/count))
                    post.rating = post_rating
                post.save()

            args = {'posts': posts, 'form':form}
            return render(request, self.template_name, args)
        else:
            if (len(list(get_messages(request)))==0):
                messages.error(request, 'Please Sign In!')
            return HttpResponseRedirect("/")

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            if(search is not None):
                posts = Post.objects.filter(name__icontains=search) #searches database based on substring
            else:
                posts = Post.objects.all() #if no search input, displays all posts
        args = {'posts': posts,'form': form}
        return render(request, self.template_name, args)

#view for individual housing posts
class PostView(TemplateView):
    template_name = 'polls/post.html'
    model = Post
    def get(self, request, post_name):
        if request.user.is_authenticated:
            post = Post.objects.get(name=post_name)

            post_rating = 0
            count = 0
            for review in post.review_set.all():
                post_rating += review.rating
                count += 1
            if (count==0):
                post.rating = 0
            else:
                post_rating = int(round(post_rating/count))
                post.rating = post_rating
            post.save()

            form = ReviewForm()
            args = {'post': post, 'form':form}
            return render(request, self.template_name, args)
        else:
            if (len(list(get_messages(request)))==0):
                messages.error(request, 'Please Sign In!')
            return HttpResponseRedirect("/")
    def post(self, request, post_name):
        form = ReviewForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            name = request.POST.get('first_name')
            avatar = request.POST.get('avatar')
            review = form.cleaned_data['review_text']
            rate = form.cleaned_data['rating']
            p = Post.objects.get(name=post_name)
            r = Review(post=p,review_text=review,rating=rate,reviewer_name=name,reviewer_username=username,profile_pic=avatar)
            r.save()
        return HttpResponseRedirect(reverse('housing:post',args=(post_name,)))

class ProfileView(TemplateView):
    template_name = 'polls/profile.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            if (len(list(get_messages(request)))==0):
                messages.error(request, 'Please Sign In!')
            return HttpResponseRedirect("/")

    def post(self, request):
        return HttpResponseRedirect("/profile/edit")

class RoommateView(TemplateView):
    template_name = 'polls/roommates.html'
    model = User
    def get(self, request):
        form = RoommateForm()
        if request.user.is_authenticated:
            persons = User.objects.all()
            args = {'persons': persons, 'form':form}
            return render(request, self.template_name, args)
        else:
            if (len(list(get_messages(request)))==0):
                messages.error(request, 'Please Sign In!')
            return HttpResponseRedirect("/")
    def post(self, request):
        form = RoommateForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            if(search is not None):
                persons = User.objects.filter(first_name__icontains=search)
            else:
                persons = User.objects.all()
        args = {'persons': persons,'form': form}
        return render(request, self.template_name, args)
    

def profile(request):
    return render(request, 'polls/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        uform = EditUserForm(request.POST, instance=request.user)
        pform = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
        if uform.is_valid():
            e = uform.cleaned_data['email']
            first = uform.cleaned_data['first_name']
            last = uform.cleaned_data['last_name']
            request.user.email = e
            request.user.first_name = first
            request.user.last_name = last
            request.user.save()
            return redirect('/profile')
    else:
        uform = EditUserForm(instance=request.user)
        pform = EditProfileForm(instance=request.user.profile)
        args = {'uform': uform, 'pform':pform}
        return render(request, 'polls/edit_profile.html', args)

def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')