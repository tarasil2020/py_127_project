from datetime import datetime

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .models import Post, Author

from .forms import PostForm
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


def add_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            saved = form.save(commit=False)
            saved.create_date = datetime.now()
            saved.update_date = datetime.now()

            saved.save()
            return HttpResponseRedirect(reverse_lazy('add_post'))

    return render(request,'polls/add_post.html',{'form':form})

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
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
    return render(request,'polls/post_detail.html',{'post':post})