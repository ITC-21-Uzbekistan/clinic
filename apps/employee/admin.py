from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'firstname',
        'lastname',
        'gender',
        'phone',
        'region',
        'created_at',
        'passport',
        'username',
        'password',
    ]
