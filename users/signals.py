from django.db.models.signals import post_save  # signal of a new sender object is saved
from django.contrib.auth.models import User  # sender object will be of 'User'
from django.dispatch import receiver  # reciever gets signal and an
from .models import Profile  # object of Profile gets created


@receiver(post_save, sender=User)  # When a user is saved
def create_profile(sender, instance, created, **kwargs):
    # above 4 args are sent by signal & conatin info about new user object

    if created:  # if user is created

        # create a new profile object for that user instance
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # save the profile of user
