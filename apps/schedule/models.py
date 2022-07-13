import datetime
import uuid

from django.db import models

from apps.employee.models import Employee


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

    class Meta:
        db_table = 'room'


class Week(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'week'


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    start_lunch = models.TimeField(default=datetime.datetime.strptime('13:00', '%H:%M').time())
    finish_lunch = models.TimeField(default=datetime.datetime.strptime('14:00', '%H:%M').time())
    week_days = models.ManyToManyField(Week)

    def __str__(self):
        return self.employee.user.firstname

    class Meta:
        db_table = 'schedule'
