from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps
def unauthenticated_user(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request)
    return wrapper

def unauthenticated_user_by_group(func):
    def wrapper(request):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='admin').exists():
                return redirect('AdminDash')  
            elif request.user.groups.filter(name='client').exists():
                return redirect('Client_Profile')   
            else:
                return func(request)
        else:
            return func(request)
    return wrapper

def allowed_roll(allowed_roll=[]):
    def decorator(func):
        @wraps(func)  # Import wraps from functools
        def wrapper(request, *args, **kwargs):  # Accept arbitrary arguments and keyword arguments
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roll:
                return func(request, *args, **kwargs)  # Pass arguments and keyword arguments to the wrapped function
            else: 
                return HttpResponse('You Are Not Allowed To Access')
        return wrapper
    return decorator

def only_admin(func):
    def wrapper(request):
        group = None
        if request.user.groups.exists():
            pass