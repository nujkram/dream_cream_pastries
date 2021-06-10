from django import forms
from branches.models.branch.models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'contact_number', 'region', 'province', 'city']
