from faker import Faker
from django_test import TestCase


from employees.models.employee.models import Employee as Master
from employees.models.employee.factories import EmployeeFactory as MasterFactory

fake = Faker()


class EmployeeTest(TestCase):
    def test_create_employee(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )