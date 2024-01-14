from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True, label='First Name')
    last_name = forms.CharField(max_length=255, required=True, label='Last Name')
    email = forms.EmailField(max_length=255, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2


class CustomUserChangeForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, label='Confirm Password')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ('email', 'password')
