from utils.AbstractUser import AbstractUser


class Employee(AbstractUser):

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = 'employee'
