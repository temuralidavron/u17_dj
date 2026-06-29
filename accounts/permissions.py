from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect


def checking_login(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:   # login qilganmi
            return redirect('login')
        return func(request,*args,**kwargs)
    return wrapper


def checking_admin(func):
    def wrapper(request,*args,**kwargs):
        print(request.user.role)
        if request.user.is_authenticated:
            if request.user.role != "admin":
                return HttpResponse("Sizga ruxsat yo'q")
        return func(request, *args, **kwargs)
    return wrapper

