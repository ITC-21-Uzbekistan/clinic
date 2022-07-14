from django.db import models

from auth_user.models import User


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

    class Meta:
        db_table = 'employee'
