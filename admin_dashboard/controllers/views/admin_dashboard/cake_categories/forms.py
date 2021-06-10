from django import forms
from cakes.models.cake_category.models import CakeCategory


class CakeCategoryForm(forms.ModelForm):
    class Meta:
        model = CakeCategory
        fields = ['name']
