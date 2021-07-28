from django.shortcuts import render
from .models import Article
# Create your views here.


def home(request):
    context={
        'articles':Article.objects.filter(status='p').order_by('-publish')
             }
    return render(request, 'news/base.html', context)

def detail(request,slug):
    context={
        'article':Article.objects.get(slug=slug)

    }

    return render(request,'news/detail.html',context)
