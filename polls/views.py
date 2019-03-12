from .forms import SuggestForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.utils import timezone
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from .models import Post, Review

class PostCreateView(CreateView):
    model = Post
    fields = ('user', 'post')

class LoginView(TemplateView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Post.objects

    def post(self, request):
        return HttpResponseRedirect("/search/")

class SearchView(TemplateView):
    template_name = 'polls/search.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = SuggestForm()
            posts = Post.objects.all()

            args = {'form': form, 'posts': posts}
            return render(request, self.template_name, args)
        else:
            return HttpResponseRedirect("/")

    def post(self, request):
        form = SuggestForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['search']
            form = SuggestForm()

            args = {'form': form, 'text': text}
        return HttpResponseRedirect("/search/results/")


class ListView(TemplateView):
    template_name = 'polls/list.html'
    def get(self, request):
        if request.user.is_authenticated:
            form = SuggestForm()
            posts = Post.objects.all()
            args = {'form': form, 'posts': posts}
            return render(request, self.template_name, args)
        else:
            return HttpResponseRedirect("/")

