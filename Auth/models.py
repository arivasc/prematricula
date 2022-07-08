from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from Schools.models import Escuela

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    dni = models.CharField(max_length=8, null=True)
    cui = models.CharField(max_length=8, null=True)
    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        null=True
    )
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Create your models here.
