from django.db import models

from utils.AbstractUser import AbstractUser


class Doctor(AbstractUser):
    REGION_CHOICE = (
        ('Tashkent', 'Tashkent'),
        ('Tashkent region', 'Tashkent region'),
        ('Andijan', 'Andijan'),
        ('Bukhara', 'Bukhara'),
        ('Fergana', 'Fergana'),
        ('Jizzakh', 'Jizzakh'),
        ('Xorazm', 'Xorazm'),
        ('Namangan', 'Namangan'),
        ('Navoiy', 'Navoiy'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Samarkand', 'Samarkand'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Surxondaryo', 'Surxondaryo'),
    )

    region = models.CharField(max_length=50, choices=REGION_CHOICE, null=True, blank=True)
    diploma = models.ImageField(upload_to='diplomas/', null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    room_number = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'doctor'

