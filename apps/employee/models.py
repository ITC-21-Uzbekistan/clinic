from utils.AbstractUser import AbstractUser


class Employee(AbstractUser):

    class Meta:
        db_table = 'employee'
