from faker import Faker
from django_test import TestCase


from branches.models.branch_menu.models import BranchMenu as Master
from branches.models.branch_menu.factories import BranchMenuFactory as MasterFactory

fake = Faker()


class BranchMenuTest(TestCase):
    def test_create_branch_menu(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )