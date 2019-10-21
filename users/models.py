from django.db import models
from django.utils import timezone

from permissions.models import Permission


class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_login = models.TimeField(default=timezone.now)
