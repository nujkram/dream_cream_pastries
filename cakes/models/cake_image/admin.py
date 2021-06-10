from django.contrib import admin

from .models import CakeImage


class CakeImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'created']
    list_filter = ['cake']
    search_fields = ['name']
    ordering = ['-created']


admin.site.register(CakeImage, CakeImageAdmin)
