from django.db import models
from django.utils import timezone


class Register(models.Model):
    username   = models.CharField(max_length=60)
    email      = models.EmailField(max_length=60)
    password   = models.CharField(max_length=60)
    login_time = models.DateTimeField(default=timezone.now,blank=True)
    login_ip   = models.GenericIPAddressField()

    def __str__(self):
        return '{s}',format(username)




