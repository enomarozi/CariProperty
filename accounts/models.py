from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_hp = models.CharField(max_length=15)
    tanggal_lahir = models.DateField()