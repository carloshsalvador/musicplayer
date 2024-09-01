# music_player_app/models.py
# the CustomUser is going to be used at form.py and admin.py
# CustomUser is a model that inherits from AbstractUser, which is the standard Django's User model.

from django.contrib.auth.models import AbstractUser
from django.db import models
 
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='user'
    )
