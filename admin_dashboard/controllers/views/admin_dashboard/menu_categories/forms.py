from django import forms
from menus.models.menu_category.models import MenuCategory


class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['name']
