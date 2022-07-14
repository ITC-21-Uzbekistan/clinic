from django.db import models

from auth_user.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_history = models.FileField(upload_to="patient_histories/", null=True, blank=True)
    analysis_history = models.FileField(upload_to="analysis_histories/", null=True, blank=True)

    class Meta:
        db_table = 'patient'
