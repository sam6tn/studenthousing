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
from housing.forms import EditUserForm, EditProfileForm, RoommateForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Review, Profile, Image

class LoginView(TemplateView):
    template_name = 'housing/index.html'

    def post(self, request):
        return HttpResponseRedirect("/housingsearch/")

#view for housing search
class ListView(TemplateView):
    template_name = 'housing/list.html'
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
                post.save(update_fields=["rating"])
            args = {'posts': posts, 'form':form}
            return render(request, self.template_name, args)
        else:
            return HttpResponseRedirect("/")

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            filter = form.cleaned_data['filter']
            if(search is not None and search is not ""):
                if (filter is not ''):
                    if (filter != "priceup"):
                        posts = Post.objects.filter(Q(name__icontains=search) |
                                                    Q(address__icontains=search) |
                                                    Q(info__icontains=search)).order_by('-'+filter)  # searches database based on substring
                    else:
                        posts = Post.objects.filter(Q(name__icontains=search) |
                                                    Q(address__icontains=search) |
                                                    Q(info__icontains=search)).order_by("price")
                else:
                    posts = Post.objects.filter(Q(name__icontains=search) |
                                                Q(address__icontains=search) |
                                                Q(info__icontains=search))
            else:
                if(filter is not ''):
                    if (filter != "priceup"):
                        posts = Post.objects.all().order_by('-'+filter)
                    else:
                        posts = Post.objects.all().order_by("price")
                else:
                    posts = Post.objects.all()
        args = {'posts': posts,'form': form, 'search':search}
        return render(request, self.template_name, args)

#view for individual housing posts
class PostView(TemplateView):
    template_name = 'housing/post.html'
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
            post.save(update_fields=["rating"])

            images = post.image_set.all()

            form = ReviewForm()
            args = {'post': post, 'form':form, 'images':images}
            return render(request, self.template_name, args)
        else:
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
    template_name = 'housing/profile.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect("/")

    def post(self, request):
        return HttpResponseRedirect("/profile/edit")

class RoommateView(TemplateView):
    template_name = 'housing/roommates.html'
    model = User
    def get(self, request):
        form = RoommateForm()
        if request.user.is_authenticated:
            persons = User.objects.all().exclude(profile__need_roommate=False)
            args = {'persons': persons, 'form':form}
            return render(request, self.template_name, args)
        else:
            return HttpResponseRedirect("/")
    def post(self, request):
        form = RoommateForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            years = form.cleaned_data['year']
            genders = form.cleaned_data['gender']
            if(search is not None and search is not ""):
                if(years and genders):
                    persons = User.objects.filter(Q(first_name__icontains=search) | Q(profile__bio__icontains=search), profile__year__in=years, profile__gender__in= genders)\
                        .exclude(profile__need_roommate=False)
                elif (years and not genders):
                    persons = User.objects.filter(Q(first_name__icontains=search) | Q(profile__bio__icontains=search), profile__year__in=years) \
                        .exclude(profile__need_roommate=False)
                elif (genders and not years):
                    persons = User.objects.filter(Q(first_name__icontains=search) | Q(profile__bio__icontains=search), profile__gender__in=genders) \
                        .exclude(profile__need_roommate=False)
                else:
                    persons = User.objects.filter(Q(first_name__icontains=search) | Q(profile__bio__icontains=search)).exclude(profile__need_roommate=False)
            else:
                if (years and genders):
                    persons = User.objects.filter(profile__year__in=years, profile__gender__in=genders) \
                        .exclude(profile__need_roommate=False)
                elif (years and not genders):
                    persons = User.objects.filter(profile__year__in=years) \
                        .exclude(profile__need_roommate=False)
                elif (genders and not years):
                    persons = User.objects.filter(profile__gender__in=genders) \
                        .exclude(profile__need_roommate=False)
                else:
                    persons = User.objects.exclude(profile__need_roommate=False)
        args = {'persons': persons,'form': form}
        return render(request, self.template_name, args)
    

# def profile(request):
#     return render(request, 'housing/profile.html')

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
        return render(request, 'housing/edit_profile.html', args)

def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')
