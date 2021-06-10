from django.db import models
from django.apps import apps


class BranchQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)


class BranchManager(models.Manager):
    def get_queryset(self):
        return BranchQuerySet(self.model, using=self._db)
    
    def actives(self):
        return self.get_queryset().actives()
    
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
