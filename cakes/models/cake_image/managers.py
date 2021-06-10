from django.db import models
from django.apps import apps


class CakeImageQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)


class CakeImageManager(models.Manager):
    def get_queryset(self):
        return CakeImageQuerySet(self.model, using=self._db)
    
    def actives(self):
        return self.get_queryset().actives()
    
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
