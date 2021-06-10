from django import forms

from accounts.models.account.models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ['email', 'user_type', 'username']
