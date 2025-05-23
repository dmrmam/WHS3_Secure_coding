from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    account_number = models.CharField(max_length=50, blank=True, null=True)
    is_banned = models.BooleanField(default=False)