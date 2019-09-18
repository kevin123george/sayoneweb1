from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegForm

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




