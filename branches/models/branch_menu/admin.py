from django.contrib import admin

from .models import BranchMenu


class BranchMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch', 'menu', 'created']
    list_filter = ['branch']
    search_fields = ['branch', 'menu']
    ordering = ['-created']


admin.site.register(BranchMenu, BranchMenuAdmin)
