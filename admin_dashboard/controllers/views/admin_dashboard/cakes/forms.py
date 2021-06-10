from django import forms
from cakes.models.cake.models import Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'price', 'category']
