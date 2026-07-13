from django.urls import path
from django.views.generic import TemplateView

from accounts import views


urlpatterns=[
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.get_profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit-profile'),
    path("send/email/", TemplateView.as_view(template_name='accounts/send.html'),name='send'),
    path("resset/email/",views.send_email_code,name='resset'),
    path("done/",views.done_password,name='done'),



]