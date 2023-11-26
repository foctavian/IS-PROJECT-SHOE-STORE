from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'role')
