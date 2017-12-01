from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',
                             widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email')
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('dob','photo')
        
