from django.urls import path
from .views import get_news, create_news, get_new, update_new, delete_new, like_new,profile

urlpatterns=[
    path('',get_news,name='list'),
    path('create/',create_news,name='create-news'),
    path('detail/<int:pk>/',get_new,name='detail-news'),
    path('update/<int:pk>/',update_new,name='update-news'),
    path('delete/<int:pk>/',delete_new,name='delete-news'),


    # like
    path("news/<int:pk>/like/", like_new, name="like_new"),
    path("news/profile/", profile, name="profile_like"),



]