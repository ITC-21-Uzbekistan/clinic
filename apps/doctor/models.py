from django.db import models

from utils.AbstractUser import AbstractUser


class Doctor(AbstractUser):
    REGION_CHOICE = (
        ('Tashkent', 'Tashkent'),
        ('Tashkent region', 'Tashkent region'),
        ('Andijan region', 'Andijan region'),
        ('Bukhara region', 'Bukhara region'),
        ('Fergana region', 'Fergana region'),
        ('Jizzakh Region', 'Jizzakh Region'),
        ('Xorazm Region', 'Xorazm Region'),
        ('Namangan Region', 'Namangan Region'),
        ('Navoiy Region', 'Navoiy Region'),
        ('Qashqadaryo Region', 'Qashqadaryo Region'),
        ('Samarkand Region', 'Samarkand Region'),
        ('Sirdaryo Region', 'Sirdaryo Region'),
        ('Surxondaryo Region', 'Surxondaryo Region'),
    )

    region = models.CharField(max_length=50, choices=REGION_CHOICE, null=True, blank=True)
    diploma = models.ImageField(upload_to='diplomas/', null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    room_number = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'doctor'

