from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from .forms import UserRegForm,UserUpdateForm,Editprofile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def home(request):
    return render (request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_index')
    else:
        form = UserRegForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
@login_required
def profile(request):
 
    return render(request, 'profile.html',)

@login_required
def edit(request):
    if request.method == 'POST':
        form = Editprofile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            print("valid")
            return redirect('profile')
    else:
        form = Editprofile(instance=request.user)
    return render(request, 'edit.html', {
        'form': form
    })


