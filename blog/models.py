from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Post(models.Model):
    
    title=models.CharField(max_length=140)
    body=models.TextField()
    date=models.DateTimeField()
    
    def __str__(self):
        return self.title
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)