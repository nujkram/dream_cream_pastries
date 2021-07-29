from django import forms
from employees.models.employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'extension',
            'contact_number',
            'file',
            'address',
            'region',
            'province',
            'city',
            'branch',
            'position',
        ]
