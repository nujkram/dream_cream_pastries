import factory
from faker import Faker

from .models import Employee as Master

fake = Faker()


class EmployeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
