import email
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):

    STATUS_CHOICES = (
            (1,'Activado'),
            (2,'Desactivado'),
    )

    reset_password=models.IntegerField(choices=STATUS_CHOICES,default=2)
    groups= models.CharField(default='Clientes',max_length=15)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default=False)
    direction=models.CharField(max_length=60, blank=True, default='')
    phone=models.CharField(max_length=7, blank=True, default='')


    def __str__(self):
        return self.username

