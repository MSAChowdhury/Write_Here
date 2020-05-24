from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import post,Comment
from blog.forms import PostFrom,CommentFrom
from django.contrib.auth.decorators import  login_required
from django.urls import reverse_lazy
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
    redirect  = 'blog/post_detail.html'

    form_class = PostFrom
    model = post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect  = 'blog/post_detail.html'

    form_class = PostFrom
    model = post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
        login_url = '/login/'
        redirect  = 'blog/post_list.html'
        model = post

        def get_queryset(self):
            return post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request,pk):
    post = get_object_or_404(post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment(request,pk):
    post = get_object_or_404(post,pk=pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_detail',pk=post.pk)
    else:
        form = CommentFrom()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
