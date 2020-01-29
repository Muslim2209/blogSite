from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    followed = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)
    blocked = models.ManyToManyField('self', related_name='blockers', symmetrical=False, blank=True)
    profile_picture = models.ImageField(upload_to='users/', blank=True)
