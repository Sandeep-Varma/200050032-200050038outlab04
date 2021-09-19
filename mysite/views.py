from django.shortcuts import render
from mysite.forms import UserForm,ProfileForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib import messages
from .models import Profile
import requests
class SignUpView(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

class UserList(ListView):
    model = User
    template_name = 'explore.html'

def ViewProfile(request,p_id):
    dict={'u': User.objects.get(pk=p_id)}
    return render(request,"profile.html",dict)
    
def updateProfile(request,p_id):
    dict={'u': User.objects.get(pk=p_id)}
    d='https://api.github.com/users/'+dict['u'].username
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
    dict['u'].profile.repo_list=l
    dict['u'].profile.followers=p['followers']
    dict['u'].profile.save()
    return render(request,"profile.html",dict)
