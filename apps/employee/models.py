from django.db import models

from auth_user.models import User
from apps.direction.models import Direction


class Employee(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    diploma = models.ImageField(
        upload_to='diplomas/',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='employees/',
        null=True,
        blank=True
    )
    experience = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    room_number = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'employee'
