from django.db import models

# Create your models here.
# models.py


# class User(models.Model):
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['email']  # Specify other required fields if necessary

    def __str__(self):
        return self.username


# class Message(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
#     receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)