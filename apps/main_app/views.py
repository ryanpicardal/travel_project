# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Trip
# Create your views here.

def home(request):
    context = {
        'cur_user': User.objects.get(id = request.session['id']),
        'user_trips': Trip.objects.filter(creator = User.objects.get(id = request.session['id'])),
        'other_trips': Trip.objects.exclude(creator = User.objects.get(id = request.session['id']))
    }
    return render(request, 'main_app/index.html', context)

def addtrip(request):
    return render(request, 'main_app/add.html')

def createtrip(request):
    Trip.objects.create(
        destination = request.POST['destination'],
        description = request.POST['description'],
        startdate = request.POST['startdate'],
        enddate = request.POST['enddate'],
        creator = User.objects.get(id = request.session['id']),
    )
    return redirect('/main/home')

def destination(request, id):
    context = {
        'trip': Trip.objects.get(id = id),
    }
    return render(request, 'main_app/destination.html', context)

def join(request, id):
    logged_user = User.objects.get(id = request.session['id'])
    target_trip = Trip.objects.get(id = id)
    target_trip.group.add(logged_user)
    return redirect('/main/home')