from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context={'message':'hello'}
    a = [1,2,3,4,5]
    context['some_list'] = a

    return render(request,'polls/index.html',context)


def home_page(request):
    return render(request, 'polls/homepage.html')