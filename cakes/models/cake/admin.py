from django.contrib import admin

from .models import Cake


class CakeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'created']
    list_filter = ['category']
    search_fields = ['name', 'category', 'price']
    ordering = ['-created']


admin.site.register(Cake, CakeAdmin)
