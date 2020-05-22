from django.shortcuts import render
from blog.models import post,Comment
from blog.forms import PostFrom,CommentFrom
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,
DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView():
    model = post

    def get_queryset(self):
        return post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetails(DetailView):
    model = post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect  = 'blog\post_detail.html'

    form_class = PostFrom
    model = post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect  = 'blog\post_detail.html'

    form_class = PostFrom
    model = post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
        login_url = '/login/'
        redirect  = 'blog\post_list.html'
        model = post

        def get_queryset(self):
            return post.objects.filter(published_date__isnull=True).order_by('created_date')
