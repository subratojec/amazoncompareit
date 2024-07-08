from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc= models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    # Note: first_name, last_name, and email are already included in AbstractUser
    # We just need to add phone_number
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username