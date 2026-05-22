from django.urls import path
from .views import get_site,get_ali,get_news

urlpatterns=[
    path('',get_news,name='list'),
    path('site/',get_site,name='site'),
    path('ali/',get_ali,name='ali'),
]