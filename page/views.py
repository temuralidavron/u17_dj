from django.shortcuts import render
from .models import News
# Create your views here.


def get_site(request):
    return render(request,'page/site.html')


def get_ali(request):
    name='ali'
    context={
        'ism':name
    }
    return render(request,'page/ali.html',context)



def get_news(request):
    news=News.objects.all()   # select * from news [{'id':1,'title':'baha sevgi'},]
    context={
        'news':news
    }
    return render(request,'page/list.html',context)
