import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_with_models.settings')
django.setup()


import random
from faker import Faker
from mysql_app.models import EmployeeDetails
#from working_with_models.first_app import models


fakegen = Faker()

def populate(NUMBER = 5):
    for entry in range(NUMBER):
        #fake data for entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        employee_details = EmployeeDetails.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]

if __name__ == "__main__":
    print("Populating script!")
    populate(20)
    print("Population completed!")


