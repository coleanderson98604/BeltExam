# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
def index(request):
    if request.session.get('id') is None:
        request.session['id'] = 0
    return render(request,'LogReg/index.html')
def register(request):
    errors = User.objects.base_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(
            name = request.POST['name'],
            username = request.POST['username'],
            password = hash1,
            birthday = request.POST['birthdate']
        )
        context = {
            'User': User.objects.last()
        }
        print type(request.POST['birthdate'])
        request.session['id'] = new_user.id
        print request.session['id']
        return redirect("/user")
def show(request):
    login = request.POST['Username']
    password = request.POST['Password']
    if len(login) < 1 or len(password) < 1:
        messages.error(request,"Fields cannot be empty")
        return redirect('/')
    else:
        errors = User.objects.login_validator(request.POST)
        user = User.objects.filter(username=login)
        request.session['id'] = user[0].id
    if len(user) < 1:
        messages.error(request,"Username or password is incorrect")
        return redirect('/')
    else:
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
            return redirect('/')
        else:
            return redirect("/user")

            