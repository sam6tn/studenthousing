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

from .models import Post, Review

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
            review = form.cleaned_data['review_text']
            p = Post.objects.get(id=post_id)
            r = Review(post=p,review_text=review)
            r.save()
        return HttpResponseRedirect(reverse('housing:post',args=(post_name,)))