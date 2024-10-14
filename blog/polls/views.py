from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import F
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .models import Post, Author, Comment

from .forms import PostForm,CommentForm
# Create your views here.

def index(request):
    context={'message':'hello'}
    a = [1,2,3,4,5]
    context['some_list'] = a

    return render(request,'polls/index.html',context)


def home_page(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    context = {'posts':posts,'authors':authors}



    return render(request, 'polls/homepage.html',context)

@login_required()
def add_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            saved = form.save(commit=False)
            saved.create_date = datetime.now()
            saved.update_date = datetime.now()
            saved.author = request.user
            print(saved)
            saved.save()
            return HttpResponseRedirect(reverse_lazy('add_post'))

    return render(request,'polls/add_post.html',{'form':form})

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    post_comments = Comment.objects.filter(post=post)
    sorted_comments = post_comments.order_by('-update_date')[:10]

    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            saved = form.save(commit=False)
            saved.create_date = datetime.now()
            saved.update_date = datetime.now()
            saved.post = post
            saved.author = request.user
            saved.save()
            form = CommentForm()
            return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))
    context = {'post': post, 'post_comments': sorted_comments, 'form': form}
    return render(request,'polls/post_detail.html',context)


def author_page(request,pk):
    author = Author.objects.get(pk=pk)
    authors_posts = Post.objects.filter(author=author)
    context={'author':author,'authors_posts':authors_posts}
    return render(request,'polls/author_page.html',context)

def add_like(request,pk):
    post = Post.objects.get(pk=pk)
    post.number_of_likes+=1
    post.save()
    print(post.number_of_likes)
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))


def post_edit(request,pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST)

class UserLogin(LoginView):
    template_name = 'polls/login.html'

class UserLogout(LoginRequiredMixin,LogoutView):
    template_name = 'polls/logout.html'

