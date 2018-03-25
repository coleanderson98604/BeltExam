# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from ..LogReg.models import *

# Create your views here.
def index(request):
    users = User.objects.filter(id = request.session['id'])
    Trips = Trip.objects.all()
    context = {
        "Trips": Trips,
        "User": users[0]
    }
    return render(request,'belt_exam/index.html',context)
def create(request):
    errors = Trip.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/user/add')
    else:   
        users = User.objects.filter(id = request.session['id'])
        Trip.objects.create(
            destination = request.POST['destination'],
            travel_datefrom = request.POST['travel_date'],
            travel_dateto = request.POST['travel_end'],
            description = request.POST['description'],
            user = users[0]
        )
        return redirect('/user')
def add(request):
    return render(request,'belt_exam/add.html')
def show(request,id):
    trips = Trip.objects.get(id=id)
    users = User.objects.all()
    context = {
        "Trip": trips,
        "User": users
    }
    return render(request,'belt_exam/show.html',context)
def logout(request):
    request.session.flush()
    return redirect('/')
def join(request,id):
    users = User.objects.get(id = request.session['id'])
    trips = Trip.objects.get(id=id)
    trips.joined.add(users)
    trips.save()
    return redirect('/user')
