from faker import Faker
from django_test import TestCase


from menus.models.menu.models import Menu as Master
from menus.models.menu.factories import MenuFactory as MasterFactory

fake = Faker()


class MenuTest(TestCase):
    def test_create_menu(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )