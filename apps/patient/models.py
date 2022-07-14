from django.db import models

from auth_user.models import User


class Patient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    potent_history = models.ImageField(null=True, blank=True)
    analis_history = models.ImageField(null=True, blank=True)



    class Meta:
        db_table = 'patient'
