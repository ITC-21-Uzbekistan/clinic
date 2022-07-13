from django.db import models

from utils.AbstractUser import AbstractUser


class Patient(AbstractUser):
    pass

    class Meta:
        db_table = 'patient'
