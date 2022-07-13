from django.db import models

from apps.employee.models import Employee


class Room(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

    class Meta:
        db_table = 'room'


class Week(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'week'


class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    week_days = models.ManyToManyField(Week)

