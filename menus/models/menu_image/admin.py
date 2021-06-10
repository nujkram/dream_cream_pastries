from django.contrib import admin

from .models import MenuImage


class MenuImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']
    list_filter = ['is_active', 'menu']
    search_fields = ['name']
    ordering = ['-created']


admin.site.register(MenuImage, MenuImageAdmin)
