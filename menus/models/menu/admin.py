from django.contrib import admin

from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_best', 'is_active', 'created']
    list_filter = ['is_best', 'is_active', 'category']
    search_fields = ['name', 'category']
    ordering = ['-created']


admin.site.register(Menu, MenuAdmin)
