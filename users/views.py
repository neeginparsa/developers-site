from django.shortcuts import render
from .models import Profile


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
