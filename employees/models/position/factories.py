import factory
from faker import Faker

from .models import Position as Master

fake = Faker()


class PositionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
