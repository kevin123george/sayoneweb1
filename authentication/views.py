from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegForm,UserUpdateForm
from django.contrib.auth.models import User
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

def profile(request):
 
    return render(request, 'profile.html',)
    



