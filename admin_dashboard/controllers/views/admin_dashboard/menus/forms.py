from django import forms
from menus.models.menu.models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'category', 'is_best']
