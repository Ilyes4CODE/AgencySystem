from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout,authenticate
from django.contrib.auth.models import User,Group
from .decorators import *
from django.contrib import messages
from .models import Profile,Reservation,Packages
from django.contrib.auth.hashers import make_password
from mainapp.models import Hotel,Rooms
# Create your views here.

@unauthenticated_user_by_group
def login_user(request):
    if request.method == "POST":
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        user = authenticate(username=email, password=password)
        
        if user is not None:
            if user.groups.filter(name='admin').exists():
                login(request, user)
                return redirect("AdminDash")
            elif user.groups.filter(name='client').exists():
                login(request, user)
                return redirect('Client_Profile') 
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'auth/login.html')

@unauthenticated_user_by_group
def SignupView(request):
    if request.method == "POST":
        newusername = request.POST.get('username')
        email = request.POST.get('email')
        passport = request.POST.get('passport')
        phone_number= request.POST.get('phone')
        password = request.POST.get('password')
        if User.objects.filter(username=newusername).exists():
            message = messages.error(request, 'Username already exists')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            message = messages.error(request, 'Email already exists')
            return redirect('signup')
        user = User.objects.create(
            username=newusername,
            email=email,
            password=make_password(password)
        )
        Profile.objects.create(user=user, passport_Number=passport, phone_number=phone_number)
        
        group = Group.objects.get(name="client")
        user.groups.add(group)
        
        message = messages.success(request, 'Account created successfully for ' + newusername)
        return redirect('login')

    return render(request, 'auth/signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

#admin
@login_required(login_url='login')
@allowed_roll(['admin'])
def AdminDash(request, status=None):
    pending_reservations = Reservation.objects.filter(is_accepted=False).order_by('-id')
    accepted_reservations = Reservation.objects.filter(is_accepted=True).order_by('-id')
    
    if status == "Pending":
        all_reservation = pending_reservations
    elif status == "Accepted":
        all_reservation = accepted_reservations
    else:
        all_reservation = pending_reservations | accepted_reservations
    
    count = all_reservation.count()
    context = {
        'res': all_reservation,
        'count': count,
    }
    return render(request, 'accounts/Admin/dashboard.html', context)

@login_required(login_url='login')
@allowed_roll(['admin'])
def get_all_clients(request):
    profiles = Profile.objects.all()
    client = [profile for profile in profiles if profile.user.groups.filter(name="client")]
    context = {
        'Clients':client
    }
    return render(request,'accounts/Admin/clients.html',context)
@login_required(login_url='login')
@allowed_roll(['admin'])
def Accepte_Demande(request,pk):
    reservation = get_object_or_404(Reservation,pk=pk)
    reservation.is_accepted = True
    reservation.save()
    return redirect('AdminDash')

@login_required(login_url='login')
@allowed_roll(['admin'])
def Admin_Packages(request):
    pack = Packages.objects.all()
    count = Packages.objects.all().count()
    context = {
        'pack':pack,
        'count':count
    }
    return render(request,'accounts/Admin/packages.html',context)

@login_required(login_url='login')
@allowed_roll(['admin'])
def Add_Packages(request):
    if request.method == 'POST':
        description = request.POST['Description'] 
        amount = request.POST['Amount']
        picture = request.FILES['Pic']
        Packages.objects.create(
            image = picture,
            Description = description,
            price = amount
        )
        return redirect('Admin_Packages')
    return render(request,'accounts/admin/add_pack.html')
##admin
##Client
@login_required(login_url='login')
@allowed_roll(['client'])
def ClientProfile(request):
    user = User.objects.get(username=request.user)
    account = Profile.objects.get(user=request.user)
    context = {
        'user':user,
        'profile':account
    }
    return render(request,'accounts/Client/account.html',context)

@login_required(login_url='login')
@allowed_roll(['client'])
def ClientSetting(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=request.user)
    old_pfp = profile.pfp
    context = {
        'user':user,
        'profile':profile
    }
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        profile.phone_number = request.POST.get('phone')
        profile.passport_Number = request.POST.get('passport')
        if 'image' in request.FILES:
            profile.pfp = request.FILES['image']
        else:
            profile.pfp = old_pfp
        user.save()
        profile.save()
        return redirect('Client_Profile')
    return render(request,'accounts/Client/account_setting.html',context)


@login_required(login_url='login')
@allowed_roll(['client'])
def Client_Packages(request):
    packages = Packages.objects.all()
    count = Packages.objects.all().count()
    context = {
        'pack':packages,
        'count' : count
    }
    return render(request,'accounts/Client/client_packges.html',context)