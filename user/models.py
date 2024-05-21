from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

# class User(models.Model):
#     username=models.CharField(max_length=100,null=False,blank=False)
#     email=models.EmailField(null=False,blank=False)
#     password=models.CharField(max_length=100)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    updated_at=models.DateTimeField(auto_now=True)
   

    def __str__(self) -> str:
        return self.username
    
