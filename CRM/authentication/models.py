from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    SALES_CONTACT = "Sales Contact"
    SUPPORT_CONTACT = "Support Contact"
    ROLE_CHOICES = ((SALES_CONTACT, "Sales Contact"), (SUPPORT_CONTACT, "Support Contact"))
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, verbose_name="Role", null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
