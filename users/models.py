from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    birth_day = models.DateField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[
        "first_name"
        "last_name"
        "email"
        "birth_day"
    ]
    