from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import Register, Login

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, '회원가입에 성공했습니다, 환영합니다!')
            return redirect('accounts:login')
    else:
        form = Register()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '로그인에 성공했습니다.')
                return redirect('cal:calendar')
            else:
                messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = Login()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('accounts:login')