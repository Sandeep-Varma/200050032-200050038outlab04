from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import requests
import json
import pytz

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    followers = models.IntegerField(default=0)
    repo_list = ArrayField(ArrayField(models.CharField(max_length=30,default=''),size=2,),size=30,default=list)
    timezone = pytz.timezone('Asia/Kolkata')
    last_updated_time = models.DateTimeField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return f'{self.user.username}'
       
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            d='https://api.github.com/users/'+instance.username
            response=requests.get(d)
            p=response.json()
            response=requests.get(d+'/repos')
            q=response.json()
            i=0
            s=[]
            for x in q:
                s.append([])
                s[i].append(x["name"])
                s[i].append(x["stargazers_count"])
                i=i+1
            l=[]
            for z in range(len(s)):
                y=0
                for x in range(len(s)):
                    if s[x][1]>s[y][1]:
                        y=x
                l.append(s[y])
                s.pop(y)
                                   
            Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name,  followers=p['followers'], repo_list=l)
            instance.profile.save()
            
