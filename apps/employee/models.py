from django.db import models

from utils.AbstractUser import AbstractUser


class Employee(AbstractUser):
    diploma = models.ImageField(upload_to='diplomas/', null=True, blank=True)
    image = models.ImageField(upload_to='employees/', null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    room_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = 'employee'
