from django.db import models
from datetime import datetime


class Todo(models.Model):
    title=models.CharField(max_length=100)
    text =models.TextField()
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    photo = models.FileField(null=True,blank=True)
    

