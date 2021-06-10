from faker import Faker
from django_test import TestCase


from menus.models.menu_category.models import MenuCategory as Master
from menus.models.menu_category.factories import MenuCategoryFactory as MasterFactory

fake = Faker()


class MenuCategoryTest(TestCase):
    def test_create_menu_category(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )