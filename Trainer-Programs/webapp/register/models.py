from __future__ import unicode_literals

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)