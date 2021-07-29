from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from django import forms
from django.urls import reverse_lazy

from cakes.models.cake_image.models import CakeImage


class CakeImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CakeImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('image', css_class='form-control-file mt-2 mb-3'),
        )

    class Meta:
        model = CakeImage
        fields = ['image']
