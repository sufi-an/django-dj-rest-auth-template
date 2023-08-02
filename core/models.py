from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
ROLE = [
    ('Faculty', 'Faculty'),
    ('Staff', 'Staff'),
     ('Admin', 'Admin'),
]


class User(AbstractUser):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=150,unique=True)
    role=models.CharField(max_length=20,choices=ROLE,default='Faculty')
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=20,blank=True,null=True)
    position=models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email