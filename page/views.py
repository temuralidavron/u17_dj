from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.permissions import  checking_admin
from page.models import News


# from .models import News
# Create your views here.


#CRUD

def get_news(request):
    news=News.objects.all()
    context={
        'news':news
    }
    return render(request,"news/list.html",context)

# @checking_login
@checking_admin
def create_news(request):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        content=request.POST.get('content')
        print(content)
        if title and content:
            News.objects.create(     # insert into (title,content)  values ('
                title=title,
                content=content
            )
            return redirect('list')
    else:
        # return HttpResponse('xatolik')
        return render(request,'news/create.html')


def get_new(request,pk=None):
    new=News.objects.get(pk=pk)   # select * from news where id=id
    context={
        'new':new
    }
    return render(request,'news/detail.html',context)


def update_new(request,pk):
    new = News.objects.get(pk=pk)
    if request.method=='POST':
        title=request.POST.get('title',new.title)
        content=request.POST.get('content',new.content)
        if title and content:
            new.title=title
            new.content=content
            new.save()
            return redirect('list')
    else:

        return render(request,'news/update.html',{'new':new})



def delete_new(request,pk):
    new=News.objects.get(pk=pk)
    if request.method=='POST':
        new.delete()
        return redirect('list')
    else:
        return render(request,'news/delete.html',{'new':new})




# like
@login_required
def like_new(request, pk):
    new = get_object_or_404(News, pk=pk)

    if request.user in new.likes.all():
        new.likes.remove(request.user)  # unlike
    else:
        new.likes.add(request.user)  # like

    return redirect("detail-news", pk=pk)




@login_required
def profile(request):
    liked_news = request.user.liked_news.all()
    return render(request, "accounts/like_profile.html", {"liked_news": liked_news})

