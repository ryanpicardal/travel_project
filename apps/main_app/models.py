# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
import datetime

# Create your models here.

class TripManager(models.Model):
    
    def tripVal(self, postData):
        results = {'errors':[], 'status': False}
        
        if len(postData['destination']) < 0:
            results['status'] = True
            results['errors'].append('Cannot leave destination empty.')
            
        if len(postData['description']) < 0:
            results['status'] = True
            results['errors'].append('Cannot leave description empty')
            
        startdate = postData['startdate']
        if len(startdate) == 10:
            year = int(startdate[:4])
            month = int(startdate[5:7])
            day = int(startdate[8:])
            if datetime.date.today() > datetime.date(year, month, day):
                results['status'] = True
                results['errors'].append('Invalid date')        
        
        enddate = postData['enddate']
        if len(enddate) == 10:
            year = int(enddate[:4])
            month = int(enddate[5:7])
            day = int(enddate[8:])
            if datetime.date.today() > datetime.date(year, month, day):
                results['status'] = True
                results['errors'].append('Invalid date')

class Trip(models.Model):
    destination = models.CharField(max_length = 50)
    description = models.CharField(max_length = 255)
    startdate = models.DateField()
    enddate = models.DateField()
    creator = models.ForeignKey(User)
    #creator of trip
    group = models.ManyToManyField(User, related_name='group')
    #group of users going on trip