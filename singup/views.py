from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *

def register(request):
    Users.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Users.name=form.cleaned_data.get('usernamedb')
            messages.success(request, f'Account created for {username}!')
            return redirect('home.html')
    else:
        form = UserCreationForm()
    return render(request,'agencies.html', {'form': form})