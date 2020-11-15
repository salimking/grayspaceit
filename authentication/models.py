from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Mainuser(models.Model):
     first_name=models.CharField(max_length=50,null=True)
     last_name=models.CharField(max_length=50,null=True)
     email=models.EmailField(max_length=50,null=True)
     password=models.CharField(max_length=50,null=True)
     def __str__(self):
         return self.first_name
        