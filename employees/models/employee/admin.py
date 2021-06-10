from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'contact_number', 'address', 'is_active', 'created']
    list_filter = ['branch', 'is_active']
    search_fields = ['first_name', 'last_name', 'address']
    ordering = ['-created']


admin.site.register(Employee, EmployeeAdmin)
