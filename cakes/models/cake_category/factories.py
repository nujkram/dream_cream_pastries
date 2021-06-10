import factory
from faker import Faker

from .models import CakeCategory as Master

fake = Faker()


class CakeCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
