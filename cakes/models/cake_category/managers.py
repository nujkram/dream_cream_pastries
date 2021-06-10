from django.db import models
from django.apps import apps


class CakeCategoryQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)


class CakeCategoryManager(models.Manager):
    def get_queryset(self):
        return CakeCategoryQuerySet(self.model, using=self._db)
    
    def actives(self):
        return self.get_queryset().actives()
    
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
