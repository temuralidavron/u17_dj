from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm, LoginForm, ProfileForm, RessetPasswordForm
from accounts.models import Profile
from accounts.utils import send_login_email
from config import settings


# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            user=form.save()
            send_mail(
                subject="Assalomu alekum Wellcome ",
                message="Siz bizda productlar sotib olishiz mumkin",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['anvartop008@gmail.com','isfan13082010@gmail.com',user.email],
                fail_silently=False

            )
            Profile.objects.create(user=user)

            user = authenticate(username=user.username, password=password)
            if user:
                print(user)
                login(request, user)
                return redirect('list')
            else:
                return redirect('register')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})



def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            # user=User.objects.filter(username=username,password=password).first()
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                send_login_email(user)
                return redirect('list')
            else:
                return redirect('register')

    else:
        form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')



def get_profile(request):
    user=request.user
    if user:
        profile=Profile.objects.get(user=user)
    else:
        return redirect('list')
    context={
        'profile':profile
    }
    return render(request,'accounts/profile.html',context)


def edit_profile(request):
    profile=None
    user=request.user
    if user:
        profile=Profile.objects.get(user=user)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            # profile.age=form.cleaned_data.get('age',profile.age)
            # profile.avtar=form.cleaned_data.get('avtar',profile.avtar)
            # profile.bio=form.cleaned_data.get('bio',profile.bio)
            # profile.save()
            form.save()
            return redirect('list')
    else:
        form=ProfileForm(instance=profile)
    return render(request,'accounts/profile_form.html',{'form':form})



# forgetpassword

def send_email_code(request):
    if request.method=='POST':
        form=RessetPasswordForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user:
                send_login_email(user)


    else:
        form=RessetPasswordForm()
    return render(request,"accounts/resset_password.html")

