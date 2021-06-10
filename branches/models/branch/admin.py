from django.contrib import admin

from .models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'contact_number', 'created']
    list_filter = ['city']
    search_fields = ['id', 'name', 'city', 'contact_number']
    ordering = ['-created']


admin.site.register(Branch, BranchAdmin)
