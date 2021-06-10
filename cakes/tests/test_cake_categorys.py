from faker import Faker
from django_test import TestCase


from cakes.models.cake_category.models import CakeCategory as Master
from cakes.models.cake_category.factories import CakeCategoryFactory as MasterFactory

fake = Faker()


class CakeCategoryTest(TestCase):
    def test_create_cake_category(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )