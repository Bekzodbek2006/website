from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    pass

class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self) :
        return self.first_name
class Chart(models.Model):
    country = models.CharField(max_length=30)
    litres = models.IntegerField(default=15)
    bottles = models.IntegerField(default=15)