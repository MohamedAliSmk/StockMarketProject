from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfileExtended


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username Or Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name')


class UserProfileExtendedForm(forms.ModelForm):
    class Meta:
        model = UserProfileExtended
        fields = ('fullName',
                'country',
                'dateOfBirth',
                'jobTitle',
                'yearsOfExperience',
                'paymentMethod',
                'subscription',
                'photo',
                'phoneNumber',
                'skills',
                'latestActivities',
                'bio',
                'twitter',
                'facebook',
                'linkedin',
                'youtube',)