from __future__ import unicode_literals

from django.db import models
from dateutil import parser
from datetime import timedelta
from datetime import datetime

# Create your models here.
class Task(models.Model):
    descriptor=models.CharField(max_length=255)
    activeState=models.BooleanField(default=True)
    doneState=models.BooleanField(default=False)
    createdOn=models.DateTimeField(auto_now_add=True)
    updatedOn=models.DateTimeField(auto_now=True,blank=True,null=True)
    
    def toggle_active_state(self):
        self.activeState = not self.activeState
        
    def __str__(self):
        return self.descriptor
        
    def set_as_done(self):
        self.doneState = True
        self.activeState = False
    
    def ph_time(self):
        current_time = self.createdOn + timedelta(hours=8)
        return(current_time)
        
        