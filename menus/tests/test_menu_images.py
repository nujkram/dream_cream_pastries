from faker import Faker
from django_test import TestCase


from menus.models.menu_image.models import MenuImage as Master
from menus.models.menu_image.factories import MenuImageFactory as MasterFactory

fake = Faker()


class MenuImageTest(TestCase):
    def test_create_menu_image(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )