from faker import Faker
from django_test import TestCase


from cakes.models.cake_image.models import CakeImage as Master
from cakes.models.cake_image.factories import CakeImageFactory as MasterFactory

fake = Faker()


class CakeImageTest(TestCase):
    def test_create_cake_image(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )