from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


def createprofile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def deleteprofile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createprofile, sender=User)
post_delete.connect(deleteprofile, sender=Profile)
