import factory
from faker import Faker

from .models import Menu as Master

fake = Faker()


class MenuFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
