from django.contrib import admin

from .models import MenuCategory


class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']
    list_filter = ['is_active']
    search_fields = ['id']
    ordering = ['-created']


admin.site.register(MenuCategory, MenuCategoryAdmin)
