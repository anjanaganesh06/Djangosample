from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        # This tells Django to use 'staff_records' instead of 'myapp_employee'
        db_table = 'staff_records'