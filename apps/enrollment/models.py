from django.db import models

from apps.patient.models import Patient
from apps.employee.models import Employee


class Enrollment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    enrollment_date = models.DateField()
    doctor = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.start_time) + "" + str(self.finish_time))

    class Meta:
        db_table = 'enrollment'
