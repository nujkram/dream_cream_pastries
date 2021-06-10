import factory
from faker import Faker

from .models import Cake as Master

fake = Faker()


class CakeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
