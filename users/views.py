from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404


def LoginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'username or password incorect')

    return render(request, 'users/login-register.html', )

def LogoutUser(request):
    logout(request)
    messages.info(request, 'user logged out')
    return redirect('login')

def RegisterUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #2 khat payiin baraye tabdil matn karbar be lowercase va sepas save
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'account was created')

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'an error has accurred during registration')
    context = {'page': page, 'form':form}
    return render(request, 'users/login-register.html', context)

def Profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)



def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskill = profile.skill_set.exclude(description__exact="")
    otherskill = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topskill': topskill, 'otherskill': otherskill}
    return render(request, 'users/user-profile.html', context)



@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects':projects}
    return render(request, 'users/account.html', context)
