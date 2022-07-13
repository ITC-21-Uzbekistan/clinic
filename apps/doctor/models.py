from django.db import models

from utils.AbstractUser import AbstractUser


class Doctor(AbstractUser):
    diploma = models.ImageField(upload_to='diplomas/', null=True, blank=True)
