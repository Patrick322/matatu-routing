from django.db import models
from django import * 
from django import Posts  

# Create your models here.
class UserProfile(models.Model):
    def userprofile_reeiver(sender,instance,created, *args, **kwargs):
        if created:
            userprofile = UserProfile.objects.create(user=instance)


        post_save.connect(userprofile_receiver, sender=setting.AUTH_USER_MODEL)    
