from django.db import models


class DirectionCategory(models.Model):
    direction = models.CharField(max_length=100)

    class Meta:
        db_table = 'direction'
