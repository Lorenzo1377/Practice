from django.db import models
from django.conf import settings
from users.models import User

class post(models.Model):
    
    user = models.ForeignKey( User , o_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    content_text = models.TextField()
    created_date = models.DateField(auto_now_add= True ,editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    
