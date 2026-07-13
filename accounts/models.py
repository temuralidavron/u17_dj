from datetime import timedelta, datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation.template import block_re

from accounts.utils import create_code


# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('reader', 'Reader'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reader')
    phone=models.CharField(max_length=15)



class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')
    age=models.IntegerField(blank=True,null=True)
    avtar=models.ImageField(upload_to='profile',default='person/avatar.jpeg',blank=True,null=True)
    bio=models.TextField(blank=True,null=True)


class Code(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='codes')
    code=models.CharField(max_length=6,default=create_code)
    expire_time=models.DateTimeField(default=datetime.now()+timedelta(minutes=2))


