import factory
from faker import Faker

from .models import Branch as Master

fake = Faker()


class BranchFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
