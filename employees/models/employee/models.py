"""
Dream Cream Pastries Project
Employee 0.0.1
Employee models
Employee

Author: Mark
"""

import uuid as uuid
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.apps import apps
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField

from .managers import EmployeeManager as manager


def file_upload_path(instance, filename):
  return f'upload/{instance}/{filename}'


class Employee(models.Model):
    # === Basic ===
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    # === Identifiers ===
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, null=True, editable=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    # === Properties ===
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    extension = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=150)
    file = models.FileField(upload_to=file_upload_path, blank=False, null=False)

    # === State ===
    is_active = models.BooleanField(default=True)
    meta = JSONField(default=dict, blank=True, null=True)

    # === Relationship Fields ===
    branch = models.ForeignKey(
        'branches.Branch',
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='employees_branch'
    )
    region = models.ForeignKey(
        'locations.Region',
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='employees_region'
    )
    province = models.ForeignKey(
        'locations.Province',
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='employees_province'
    )
    city = models.ForeignKey(
        'locations.City',
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='employees_city'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='employees_created_by_user'
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='employees_updated_by_user'
    )

    objects = manager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    ################################################################################
    # === Magic Methods ===
    ################################################################################
    def __str__(self):
        return self.name    

    ################################################################################
    # === Model overrides ===
    ################################################################################
    def clean(self, *args, **kwargs):
        # add custom validation here
        super().clean()

    def save(self, *args, **kwargs):
        # self.full_clean()
        super().save(*args, **kwargs)

    ################################################################################
    # === Model-specific methods ===
    ################################################################################


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=Employee)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=Employee)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
