from django.contrib import admin

from .models import CakeCategory


class CakeCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['-created']


admin.site.register(CakeCategory, CakeCategoryAdmin)
