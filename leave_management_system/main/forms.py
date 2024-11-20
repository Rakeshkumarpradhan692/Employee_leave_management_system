from django import forms
from django.contrib.auth.models import User

class EmployeeSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
