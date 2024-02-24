from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
            

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('cal:calendar')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})
