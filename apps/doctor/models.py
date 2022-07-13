from django.db import models

from utils.AbstractUser import AbstractUser


class Doctor(AbstractUser):
    diploma = models.ImageField(upload_to='diplomas/', null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    room_number = models.PositiveIntegerField(null=True, blank=True)

