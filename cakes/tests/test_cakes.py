from faker import Faker
from django_test import TestCase


from cakes.models.cake.models import Cake as Master
from cakes.models.cake.factories import CakeFactory as MasterFactory

fake = Faker()


class CakeTest(TestCase):
    def test_create_cake(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )