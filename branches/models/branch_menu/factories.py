import factory
from faker import Faker

from .models import BranchMenu as Master

fake = Faker()


class BranchMenuFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
