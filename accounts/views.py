from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new user object but avoid saving it yet
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile=Profile.objects.create(user=new_user)
            return render(request,
                          'accounts/register_done.html',
                          {'new_user':new_user})
        else:
            user_form=UserRegistrationForm()
    else:
        user_form=UserRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form':user_form})



@login_required
def feed(request):
    return render(request,
                  'accounts/feed.html',
                  {'section':'feed'})

@login_required
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,
                               data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,
                                     data=request.POST,
                                     files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,'Error updating your profile')
            user_form=UserEditForm(instance=request.user)
            profile_form=ProfileEditForm(instance=request.user.profile)
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'accounts/edit.html',
                  {'user_form': user_form,
                   'profile_form':profile_form})
