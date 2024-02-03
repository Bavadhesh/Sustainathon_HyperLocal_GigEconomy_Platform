from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ServiceProvider(models.Model):
       user = models.OneToOneField(User,on_delete=models.CASCADE)
       Name = models.CharField(max_length=500)
       category = models.CharField(max_length=500)
       description = models.TextField()
       lat = models.FloatField()
       long = models.FloatField()
       contactno = models.CharField(max_length=50)
       Whatsappno = models.CharField(max_length=50)
       available = models.BooleanField(default=False)
       email = models.EmailField(blank=True)
       profilePhoto = models.ImageField(upload_to='Lsp/',blank=True)

class RequestBox(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customerName = models.CharField(max_length=100)
    customerPhone = models.CharField(max_length=30)
    customerAddress = models.TextField()
    customerEmail = models.EmailField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    problem = models.TextField(blank=True)
    accepted = models.BooleanField(blank=True,default=False)

class Booklogs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customerName = models.CharField(max_length=100)
    customerPhone = models.CharField(max_length=30)
    customerAddress = models.TextField()
    customerEmail = models.EmailField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    
          
       