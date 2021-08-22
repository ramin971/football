from django.shortcuts import render,get_object_or_404
from .models import Article
from jalali_date import datetime2jalali,date2jalali
# Create your views here.


def home(request):
    context={
        'articles':Article.objects.filter(status='p').order_by('-publish'),
             }

    return render(request, 'news/base.html', context)

def detail(request,slug):
    context={
        'article':get_object_or_404(Article,slug=slug,status='p')

    }

    return render(request,'news/detail.html',context)
