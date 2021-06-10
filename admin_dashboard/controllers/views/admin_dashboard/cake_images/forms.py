from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms

from cakes.models.cake_image.models import CakeImage


class CakeImageForm(forms.ModelForm):
    class Meta:
        model = CakeImage
        fields = ['image']

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('image', css_class='form-control-file mt-2 mb-3'),
    )
