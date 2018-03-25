# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

class LoginManager(models.Manager):
    def base_validator(self,postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "name should be atleast 2 characters"
        if len(postData['username']) < 3:
            errors["username"] = "username should be atleast 2 characters"
        # if len(postData['last_name']) < 3:
        #     errors["last_name"] = "Last name should be atleast 2 characters"
        if not re.match('^[a-z]*$',postData['name']):
            errors["characters"] = "Name must contain only letters"
        if not re.match('^[a-z]*$',postData['username']):
            errors["characters"] = "Username must contain only letters"
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors["email"] = "Must be a valid email"
        if postData['password'] < 8:
            errors["PasswordLength"] = "Must be longer than 8 characters"
        if postData['password'] != postData['Cpassword']:
            errors["PasswordMatch"] = "Passwords don't match"
        for usernames in User.objects.all():
            if postData['username'] == usernames.username:
                errors["UsernameMatch"] = "Username already exists"
        if not postData['birthdate']:
            errors['BirthdateField'] = "Birthdate field cannot be empty"
        if postData['birthdate']:
            if datetime.datetime.strptime(postData['birthdate'], '%Y-%m-%d') > datetime.datetime.now() - datetime.timedelta(days=365*18):
                errors['ValidDate'] = "Birthdate must be atleast 18 years ago"
        return errors
    def login_validator(self,postData):
        errors = {}
        username = postData['Username']
        passwords = postData['Password']
        user = User.objects.get(username = username)
        cpasword = bcrypt.checkpw(passwords.encode(),user.password.encode())
        if cpasword:
            return errors
        else:
            errors['login'] = "Email or password is incorrect"
            return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = LoginManager()







    