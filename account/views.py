# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import IntegrityError


# Create your views here.
def register (request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username and password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return HttpResponseRedirect("/clusters/")
            except IntegrityError:
                return render(request, 'register.html', context={'error': '用户名已存在'})
        else:
            return render(request, 'register.html', context={'error': '用户名和密码不能为空'})
    else:
        return render(request, 'register.html')


def login (request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/clusters/")
        else:
            return render(request, 'login.html', context={
                'message': {
                    'error': '用户名或密码不正确'
                }
            })
    else:
        return render(request, 'login.html')


def logout (request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')