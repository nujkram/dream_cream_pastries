from faker import Faker
from django_test import TestCase


from employees.models.position.models import Position as Master
from employees.models.position.factories import PositionFactory as MasterFactory

fake = Faker()


class PositionTest(TestCase):
    def test_create_position(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )