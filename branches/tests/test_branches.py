from faker import Faker
from django_test import TestCase


from branches.models.branch.models import Branch as Master
from branches.models.branch.factories import BranchFactory as MasterFactory

fake = Faker()


class BranchTest(TestCase):
    def test_create_branch(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )