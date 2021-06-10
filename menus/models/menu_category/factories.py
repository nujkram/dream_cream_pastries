import factory
from faker import Faker

from .models import MenuCategory as Master

fake = Faker()


class MenuCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
