from django.db import models
import datetime as dt
from django .contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField 

# Create your models here.
class UserProfile(models.Model):
    def userprofile_reeiver(sender,instance,created, *args, **kwargs):
        if created:
            userprofile = UserProfile.objects.create(user=instance)


        post_save.connect(userprofile_receiver, sender=setting.AUTH_USER_MODEL)    
