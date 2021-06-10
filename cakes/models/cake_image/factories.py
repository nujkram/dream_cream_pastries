import factory
from faker import Faker

from .models import CakeImage as Master

fake = Faker()


class CakeImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
