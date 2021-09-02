from common.models import BaseModel
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser, BaseModel):
    objects = UserManager()
    email = models.EmailField(blank=False, null=False, unique=True, db_index=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True, unique=True)
    country_code = models.CharField(max_length=4, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.CharField(max_length=512, blank=True, null=True)
    profile_picture_url = models.URLField(max_length=128, blank=True, null=True)
    following_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)
    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "User"
        swappable = "AUTH_USER_MODEL"
