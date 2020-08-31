from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.first_name
