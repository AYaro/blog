from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from typing import List, Any, Optional
from blog.base import BaseModel, DeletedManagerMixin


class UserManager(BaseUserManager, DeletedManagerMixin):
    use_in_migrations = True
    
    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> 'User':
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> 'User':
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    description = models.TextField()

    objects = UserManager()
    USERNAME_FIELD = 'email'

