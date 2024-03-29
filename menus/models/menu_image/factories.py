import factory
from faker import Faker

from .models import MenuImage as Master

fake = Faker()


class MenuImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
