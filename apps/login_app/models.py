# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
import re #imports regular expressions
import bcrypt 

# Create your models here.

class UserManager(models.Manager):
    
    def loginVal(self, postData):
        results = {'errors':[], 'status': False, 'user': None}
        email_matches = self.filter(email=postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Please check your email and password and try again.')
            results['status'] = True
        else:
            results['user'] = email_matches[0]
#            bcrypt.checkpw('test'.encode(), hash1)
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check your email and password and try again.')
                results['status'] = True
        return results
    
    def createUser(self, postData):
        #password = bcrypt.hashpw('test', bcrypt.gensalt()) #insert postData['password'] in first parameter
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        print password
        self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = password)
    
    def registerVal(self, postData):
        #validator - shows error messages to user
        results = {'errors':[], 'status': False}
        
        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short.')  
            
#        if not postData['first_name'].isalpha():
#            results['status'] = True
#            results['errors'].append('Please use alphanumeric characters only.')
        
        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short.')
            
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = True
            results['errors'].append('Not a valid email.')
        
        if len(postData['password']) < 3:
            results['status'] = True
            results['errors'].append('Password is too short.')
            
        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match')
            
        user = self.filter(email = postData['email'])
        
        if len(user) > 0:
            results['status'] = True
            results['errors'].append('Email already exists in database.')
        
        birthday = postData['birthday']
        if len(birthday) == 10:
            byear = int(birthday[:4])
            bmonth = int(birthday[5:7])
            bday = int(birthday[8:])
            if datetime.date.today() < datetime.date(byear, bmonth, bday):
                results['status'] = True
                results['errors'].append('Invalid birthdate')
        else:
            results['status'] = True
            results['errors'].append('Not a valid birthday.')
        return results
    
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = UserManager()