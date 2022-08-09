from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# HERE IS THE ENTIRE DJANGO FORM STRUCTURE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True, default=0)
    city = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=11, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    image_profile = models.ImageField(default='user.png', upload_to='users/', null=True, blank=True)
    date_regist = models.DateField(null=True, blank=True, auto_created=True, auto_now=True)

    def __str__(self) :
        return self.user.username # RETORNA NO ADMIN DO DJANGO

# THE CODE BELOW VERIFIES THE USER AND CREATES A GROUP FOR IT TO BE ADDED
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_staff:
        try:
            group = Group.objects.get(name='admin')
            group = Group.objects.get(name='Owner')
        except:
            group = Group.objects.create(name='admin')
            group = Group.objects.create(name='Owner')
    else:
        try:
            group = Group.objects.get(name='client')
        except:
            group = Group.objects.create(name='client')

    instance.groups.add(group)
    if created:
        Profile.objects.create(user=instance)

#HERE SAVE ALL INFORMATION FROM THE PROFILE INFORMED ABOVE
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()