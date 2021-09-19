from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name')

class ProfileForm(UserForm):
    class Meta:
        model = User
        fields = ()
