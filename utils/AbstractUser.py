import uuid

from django.db import models


class AbstractUser(models.Model):
    GENDER_CHO0ICE = (
        ('male', 'male'),
        ('female', 'female'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHO0ICE, null=True, blank=True)
    phone = models.PositiveBigIntegerField(max_length=15, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    passport = models.ImageField(upload_to='passports/', null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True
