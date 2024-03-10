from django.shortcuts import render
from Auth.decorators import unauthenticated_user_by_group
from .models import Packages
# Create your views here.
@unauthenticated_user_by_group
def index(request):
    last_six = Packages.objects.all().order_by('-id')[:6][::-1]
    context = {
        'pack': last_six
    }
    return render(request,'main/index.html',context)

@unauthenticated_user_by_group
def packages(request):
    last_six = Packages.objects.all().order_by('-id')[:6][::-1]
    context = {
        'pack': last_six
    }
    return render(request, 'main/packages.html', context)

@unauthenticated_user_by_group
def About(request):
    return render(request,'main/about.html')
@unauthenticated_user_by_group
def Contact(request):
    return render(request,'main/contact.html')