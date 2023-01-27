from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from apps.user.forms import LoginForm, RegisterForm


def user_login(request):
    error = None
    breadcrumbs = {
        'current': 'Вход'
    }
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
        error = 'Неправильные логин или пароль'

    return render(request, 'user/login.html', {'error': error,'breadcrumbs':breadcrumbs})


def user_register(request):
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'user/welcome.html',{'user':user})
        error = form.errors
    breadcrumbs = {
        'current': 'Регистрация'
    }
    return render(request,'user/register.html',{'error':error,'breadcrumbs':breadcrumbs})


def user_logout(request):
    logout(request)
    return redirect('index')