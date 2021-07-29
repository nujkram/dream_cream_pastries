from django import forms
from positions.models.position.models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
