from django.db import models
from django.conf import settings

class signup(models.Model):
    username = models.CharField(max_length=400)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class verify(models.Model):
    user = models.OneToOneField(signup, on_delete=models.CASCADE, primary_key=True)
    smscode = models.CharField(max_length=20)

    def __str__(self):
        return self.smscode
