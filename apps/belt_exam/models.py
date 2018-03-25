# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..LogReg.models import *
import re
import bcrypt
import datetime
# Create your models here.
class TripManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors['destination'] = "Destination cannot be empty"
        if len(postData['description']) < 1:
            errors['description'] = "Description cannot be empty"
        if not postData['travel_date']:
            errors['dateform'] = "Must have a starting date"
        if not postData['travel_end']:
            errors['dateto'] = "Must have an ending date"
        if postData['travel_date'] and postData['travel_end']:
            if datetime.datetime.strptime(postData['travel_date'], '%Y-%m-%d') < datetime.datetime.now():
                errors['ValidFrom'] = "Must be after current date"
            if datetime.datetime.strptime(postData['travel_end'],'%Y-%m-%d') < datetime.datetime.strptime(postData['travel_date'], '%Y-%m-%d'):
                errors['ValidTo'] = "Cannot end before the starting date"
        return errors
            
class Trip(models.Model):
    destination = models.CharField(max_length=255)
    travel_datefrom = models.DateField()
    travel_dateto = models.DateField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name = "trips")
    joined = models.ManyToManyField(User, related_name="Trips_joined")
    objects = TripManager()