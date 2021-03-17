#post_save gets fired after an object is
from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when a user is saved, it will send a signal. Create_profile function receives the signal and creates a profile object with the user.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# save the profile after it is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()