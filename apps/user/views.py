from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from apps.user.forms import LoginForm


# Create your views here.
def user_login(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user:
                login(request,user)
                return render('index')
        error = 'Не правельные логин/пароль'
    return render(request,'user/login.html',{'error':error})